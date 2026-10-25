#!/usr/bin/env python3
"""Testes cegos parciais (SD) da base V2; NAO le coluna 'alertas' para detectar.
Compara ao gabarito apenas apos concluir deteccao, para mensurar limitacoes.
"""
import csv,gzip,collections,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent.parent
DATA=ROOT/'dados_sinteticos_v2/imobilizado_500000_v2_REGERADO.csv.gz'
TRUTH=ROOT/'dados_sinteticos_v2/gabarito_v2_SEPARADO.csv'
OUT=ROOT/'analises';OUT.mkdir(exist_ok=True)
docs=collections.defaultdict(list); reasons=collections.defaultdict(set); balance=collections.Counter();ids=set(); n=0
with gzip.open(DATA,'rt',encoding='utf-8') as f:
 for r in csv.DictReader(f):
  aid=r['id_ativo'];assert aid not in ids;ids.add(aid);n+=1
  balance[r['escopo_dfp_2025']]+=int(r['valor_liquido_rs'])
  docs[r['documento_sintetico']].append(aid)
  if r['data_aquisicao_original']>'2025-12-31':reasons[aid].add('CORTE_POSTERIOR_A_2025')
  if int(r['vida_util_anos_modelada'])>80:reasons[aid].add('VIDA_UTIL_ACIMA_DE_80_ANOS')
for doc,group in docs.items():
 if len(group)>1:
  for aid in group:reasons[aid].add('DOCUMENTO_REPETIDO')
assert n==500000 and sum(balance.values())==25570358000
truth=collections.defaultdict(set)
with TRUTH.open(encoding='utf-8') as f:
 for r in csv.DictReader(f):truth[r['id_ativo']].add(r['anomalia_plantada'])
detected=set(reasons); planted=set(truth)
summary={'classificacao':'SD — teste baseado apenas em campos analiticos, sem acesso a dados reais','populacao':n,'saldo_por_escopo_rs':dict(balance),'ids_detectados_sem_ler_alertas':len(detected),'ids_com_anomalia_plantada':len(planted),'verdadeiros_positivos_por_id':len(detected&planted),'falsos_positivos_por_id':len(detected-planted),'nao_detectados_por_id':len(planted-detected),'contagem_marcadores_por_tipo':dict(collections.Counter(code for codes in reasons.values() for code in codes)),'limites':'Nao testa suporte documental: dados sem arquivos reais. Regra de vida util >80 anos e criterio DIDATICO. Duplicata sinaliza ambas as pontas. Alertas sintéticos nao equivalem a distorções monetárias; nenhuma extrapolacao de perdas para Auren.'}
(OUT/'PT530_V2_TESTE_INDEPENDENTE_SEM_COLUNA_ALERTAS.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
with (OUT/'PT530_V2_EXCECOES_DETECTADAS.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['id_ativo','regras_acionadas_SD'])
 for aid in sorted(reasons):w.writerow([aid,';'.join(sorted(reasons[aid]))])
print(json.dumps(summary,ensure_ascii=False))
