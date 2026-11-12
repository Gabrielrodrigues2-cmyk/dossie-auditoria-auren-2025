#!/usr/bin/env python3
"""V3 EXPERIMENTAL: 500k synthetic PPE assets, separate gross/depreciation/PPA reconciliation to Note 13(a).
Not accounting ledger of Auren; only mathematical calibration of illustrative data.
"""
import csv,gzip,random,hashlib,json,pathlib,io,collections
ROOT=pathlib.Path(__file__).resolve().parent.parent
OUT=ROOT/'dados_sinteticos_v3'; OUT.mkdir(exist_ok=True)
SEED=20251025; rng=random.Random(SEED)
N_OP=497280; N_ROU=2720
# 2025 DFP Note 13(a), physical PDF page 96, values in R$ x 1,000 converted into BRL
T={'custo':42273221000,'dep':17822049000,'ppa':1230019000,'amort_ppa':250944000}
assert T['custo']-T['dep']+T['ppa']-T['amort_ppa']==25430247000
# Oversize items model individual power generation plants (FICTIONAL asset IDs): 40 anchors account for 62% of gross PPE.
N_ANCHOR=40
anchor_w=[rng.randint(8000,18000) for _ in range(N_ANCHOR)]
other_w=[max(1,int(rng.lognormvariate(1.4,1.12))) for _ in range(N_OP-N_ANCHOR)]
weights=anchor_w+other_w
# Assign 62% to 40 anchor assets; other 38% to many smaller units.
def allocate(target,weights):
 s=sum(weights);a=[target*w//s for w in weights];a[0]+=target-sum(a);return a
cost=allocate(T['custo']*62//100,anchor_w)+allocate(T['custo']-T['custo']*62//100,other_w)
# Per-asset depreciation in [26%-58%] of original cost, then adjust to Note13 value within capacities.
rates=[rng.randint(26,58)/100 for _ in range(N_OP)]
dep=[int(c*r) for c,r in zip(cost,rates)]
diff=T['dep']-sum(dep)
# spread correction over anchors subject to 0 <= depreciation <= cost
for i in sorted(range(N_ANCHOR),key=lambda k:cost[k],reverse=True):
 if diff==0:break
 change=min(diff,cost[i]-dep[i]) if diff>0 else max(diff,-dep[i])
 dep[i]+=change;diff-=change
assert diff==0 and sum(dep)==T['dep'] and all(d<=c for d,c in zip(dep,cost))
# PPA allocated to 40 large assets; negative impacts follow proportion of positive PPA.
ppa=allocate(T['ppa'],anchor_w)+[0]*(N_OP-N_ANCHOR)
amort=allocate(T['amort_ppa'],anchor_w)+[0]*(N_OP-N_ANCHOR)
# gross ROU scope separately: net DFP ROU 140,111 (thousand), but gross/dep fictional
rou_w=[rng.randint(10,250) for _ in range(N_ROU)]
rou_cost=allocate(210000000,rou_w);rou_dep=allocate(69889000,rou_w)
assert sum(rou_cost)-sum(rou_dep)==140111000
fields=['id_ativo','escopo_dfp_2025','classe_sintetica','porte_modelado','custo_bruto_rs','depreciacao_acumulada_rs','mais_valia_ppa_rs','amortizacao_ppa_rs','valor_liquido_rs','ano_inicio_operacao','vida_util_modelada_anos','documento_sintetico']
path=OUT/'IMOBILIZADO_500000_V3_CEGO.csv.gz'; truth=OUT/'GABARITO_V3_RESTRITO.csv'
acc=collections.Counter(); classes=collections.Counter()
with open(path,'wb') as raw, open(truth,'w',encoding='utf-8',newline='') as tr:
 tw=csv.writer(tr);tw.writerow(['id_ativo','tipo_anomalia_plantada'])
 with gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0,compresslevel=6) as zipped:
  with io.TextIOWrapper(zipped,encoding='utf-8',newline='') as stream:
   w=csv.writer(stream,lineterminator='\n');w.writerow(fields)
   for ix in range(N_OP+N_ROU):
    anchor=ix<N_ANCHOR;ope=ix<N_OP
    if ope:
     j=ix;g,d,p,a=cost[j],dep[j],ppa[j],amort[j]
     scope='IMOBILIZADO_OPERACAO';kind=('USINA_GERACAO_GRANDE' if anchor else rng.choice(['MAQUINAS_E_INSTALACOES','EDIFICACOES','PECAS_E_COMPONENTES','OBRAS_E_MELHORIAS']))
    else:
     j=ix-N_OP;g,d,p,a=rou_cost[j],rou_dep[j],0,0
     scope='DIREITO_USO_ARRENDAMENTO';kind='DIREITO_DE_USO'
    net=g-d+p-a;aid=f'V3-ATV-{ix+1:07d}'; life=rng.choice([15,20,25,30,40]);yr=rng.randint(2004,2025)
    doc=f'V3-DOC-{ix+1:07d}'
    if (ix+1)%1499==0:yr=2026;tw.writerow([aid,'DATA_APOS_CORTE'])
    if (ix+1)%1999==0:life=99;tw.writerow([aid,'VIDA_UTIL_ATIPICA'])
    if (ix+1)%2499==0:doc=f'V3-DOC-{ix:07d}';tw.writerow([aid,'DOCUMENTO_REPETIDO'])
    if (ix+1)%997==0:tw.writerow([aid,'SUPORTE_NAO_DISPONIVEL'])
    w.writerow([aid,scope,kind,'ANCORA_ALTO_VALOR' if anchor else 'PULVERIZADO',g,d,p,a,net,yr,life,doc]);classes[kind]+=1
    for key,v in [('custo',g),('dep',d),('ppa',p),('amort_ppa',a),('liquido',net)]:acc[f'{scope}_{key}']+=v
assert all(acc[f'IMOBILIZADO_OPERACAO_{k}']==v for k,v in T.items())
assert acc['IMOBILIZADO_OPERACAO_liquido']==25430247000
assert acc['DIREITO_USO_ARRENDAMENTO_liquido']==140111000
rep={'natureza':'SD / inteiramente fictício; valores agregados calibrados por convenção didática, não saldos analíticos extraídos da companhia','base':'V3 CEGA SEM COLUNA DE ANOMALIAS','semente':SEED,'registros':N_OP+N_ROU,'total_liquido':sum(v for k,v in acc.items() if k.endswith('_liquido')),'composicao_rs':dict(acc),'categorias':dict(classes),'peso_40_itens_ancora_no_custo_operacional_pct':62,'origem_RP':'DFP 2025, Nota 13(a), página física 96; direito de uso em BP/nota explicativa distinta','sha256_csv_gz':hashlib.sha256(path.read_bytes()).hexdigest(),'sha256_gabarito':hashlib.sha256(truth.read_bytes()).hexdigest()}
(OUT/'CONCILIACAO_V3.json').write_text(json.dumps(rep,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'registros':rep['registros'],'total_liquido':rep['total_liquido'],'sha256':rep['sha256_csv_gz']},ensure_ascii=False))
