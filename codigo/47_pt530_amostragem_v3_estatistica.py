#!/usr/bin/env python3
"""PT530: attribute sampling on V3 synthetic assets; ex ante criterion and reproducible selection.
Separate design for 450 operating and 150 right-of-use items, plus 40 certainty units.
No monetary misstatement projection; no claims of assurance on Auren.
"""
from pathlib import Path
from collections import Counter,defaultdict
import csv,gzip,json,math,random,hashlib
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'analises';OUT.mkdir(exist_ok=True)
SRC=ROOT/'dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz'
TRUTH=ROOT/'dados_sinteticos_v3/GABARITO_V3_RESTRITO.csv'
SEED=20261111; alpha=.05; tol=.02
# One-sided Clopper-Pearson upper limit: invert binomial lower-tail, using stable recurrence.
def binom_cdf(k,n,p):
 if p<=0:return 1.
 if p>=1:return 0. if k<n else 1.
 if k>=n:return 1.
 q=1-p;term=math.exp(n*math.log(q));s=term
 for j in range(k):
  term *= (n-j)/(j+1)*p/q;s+=term
 return min(1.,s)
def upper_cp(k,n,alpha=.05):
 if k>=n:return 1.
 lo,hi=0.,1.
 for _ in range(75):
  mid=(lo+hi)/2
  if binom_cdf(k,n,mid)>alpha:lo=mid
  else:hi=mid
 return (lo+hi)/2
# Detection rules only on fields visible in blind population.
# Record/document duplication requires global observations; a year or life is visible directly.
by_scope=defaultdict(list);docids=defaultdict(list);ids=set();anchors=[]
with gzip.open(SRC,'rt',encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f):
  aid=r['id_ativo'];assert aid not in ids;ids.add(aid)
  by_scope[r['escopo_dfp_2025']].append(r);docids[r['documento_sintetico']].append(aid)
  if r['porte_modelado']=='ANCORA_ALTO_VALOR':anchors.append(r)
assert len(ids)==500000 and len(anchors)==40
# Ex ante n: 150 with zero deviations has CP95 upper ~1.977%, below tolerance 2%; 450 gives opportunity for up to a few observable exceptions.
allocation={'IMOBILIZADO_OPERACAO':450,'DIREITO_USO_ARRENDAMENTO':150}
rng=random.Random(SEED);sample=[]
for scope,n in allocation.items():sample+=rng.sample(by_scope[scope],n)
selected_ids={r['id_ativo'] for r in sample}; certainty_ids={r['id_ativo'] for r in anchors}
duplicate_ids={id for x in docids.values() if len(x)>1 for id in x}
def flags(r):
 a=[]
 if int(r['ano_inicio_operacao'])>2025:a.append('DATA_APOS_CORTE')
 if int(r['vida_util_modelada_anos'])>60:a.append('VIDA_UTIL_ATIPICA')
 if r['id_ativo'] in duplicate_ids:a.append('DOCUMENTO_REPETIDO_OU_COLISAO')
 if int(r['valor_liquido_rs'])<0:a.append('SALDO_LIQUIDO_NEGATIVO')
 return a
rows=[]; sums=defaultdict(int);ks=Counter()
for r in sorted(sample,key=lambda z:z['id_ativo']):
 f=flags(r);k=r['escopo_dfp_2025'];ks[k]+=bool(f);sums[k]+=int(r['valor_liquido_rs'])
 rows.append({'id_ativo':r['id_ativo'],'escopo':k,'valor_liquido_rs':r['valor_liquido_rs'],'procedimento':'AMOSTRAGEM_ALEATORIA_ESTRATIFICADA','teste_ano':int(r['ano_inicio_operacao'])>2025,'teste_vida_util':int(r['vida_util_modelada_anos'])>60,'teste_doc_duplicado':r['id_ativo'] in duplicate_ids,'alertas_observaveis':'|'.join(f),'resultado':'EXCECAO_SD' if f else 'SEM_EXCECAO_OBSERVAVEL_SD'})
with (OUT/'PT530_V3_AMOSTRA_E_TESTES_600.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
certainty=[]
for r in anchors:
 f=flags(r)
 certainty.append({'id_ativo':r['id_ativo'],'custo_bruto_rs':r['custo_bruto_rs'],'valor_liquido_rs':r['valor_liquido_rs'],'alertas_observaveis':'|'.join(f),'classificacao':'CERTEZA_ALTO_VALOR_SEM_INFERENCIA'})
with (OUT/'PT530_V3_ITENS_CERTEZA_40.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(certainty[0]));w.writeheader();w.writerows(certainty)
summary=[]
for scope,n in allocation.items():
 k=ks[scope];ub=upper_cp(k,n)
 summary.append({'estrato':scope,'N':len(by_scope[scope]),'n':n,'desvios_detectaveis_observados':k,'taxa_amostral':k/n,'limite_superior_unilateral_95_CP':ub,'taxa_toleravel_planejamento':tol,'conclusao':'LIMITE_SUPERIOR_ACIMA_TOLERANCIA' if ub>tol else 'LIMITE_SUPERIOR_ATE_TOLERANCIA','escopo':'Atributos visíveis fictícios; não inferir erro monetário'})
with (OUT/'PT530_V3_INTERVALOS_E_DECISAO.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
# Only now access separate truth ledger: diagnostic sensitivity on synthetic planted exceptions, not included in sampling selection.
truth=defaultdict(set)
with TRUTH.open('r',encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f):truth[r['id_ativo']].add(r['tipo_anomalia_plantada'])
detected={r['id_ativo'] for r in rows if r['alertas_observaveis']}; t_selected=set(selected_ids)&set(truth)
coverage={'selecionados_com_plantio':len(t_selected),'detectados_no_conjunto_selecionado':len(detected),'detectados_plantados':len(detected&t_selected),'selecionados_plantados_nao_detectados':len(t_selected-detected),'detectados_sem_plantio':len(detected-t_selected),'denominador':len(selected_ids)}
report={'natureza':'SD EXCLUSIVAMENTE; NAO AMOSTRA DE CONTAS REAIS DA AUREN','base_primaria':'V3','seed':SEED,'N':len(ids),'n':len(selected_ids),'estratos':summary,'itens_certeza':len(anchors),'certos_ja_na_amostra':len(certainty_ids&selected_ids),'regra_aceitacao':'comparar limite superior unilateral Clopper-Pearson (binomial conservador) a taxa toleravel de 2% por estrato; controle matematico, nao seguranca de auditoria','confianca_planejamento':.95,'limite_95_sem_desvios_n150':upper_cp(0,150),'avaliacao_gabarito_somente_apos_criterio':coverage,'avisos':['desvios sao apenas atributos sintéticos observáveis; não são fraude nem distorção da Auren','suporte indisponível no gabarito não é detectável em uma base sem documentos independentes','n=600 e 40 itens de certeza não são MUS e não permitem projetar montantes monetários','a aproximação binomial é conservadora em relação a amostragem finita sem reposição e pressupõe amostragem equiprovável dentro de cada estrato','amostragem por atributos é distinta do exame dos 40 itens de certeza']}
(OUT/'PT530_V3_PLANO_E_RESULTADOS.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'n':600,'certeza':40,'estratos':summary,'gabarito':coverage},ensure_ascii=False))
