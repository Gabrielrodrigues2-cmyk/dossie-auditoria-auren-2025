#!/usr/bin/env python3
"""Verifica dados V2 e separa gabarito do processo de detecção."""
import csv,gzip,collections,pathlib,json,hashlib,sys
root=pathlib.Path(__file__).resolve().parents[1];p=root/'dados_sinteticos_v2/imobilizado_500000_v2_REGERADO.csv.gz'
counts=collections.Counter(); sums=collections.Counter();docs=collections.Counter(); ids=set(); alertas=collections.Counter()
with gzip.open(p,'rt',encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f):
  counts['linhas']+=1;ids.add(r['id_ativo']);sums[r['escopo_dfp_2025']]+=int(r['valor_liquido_rs']);docs[r['documento_sintetico']]+=1
  assert int(r['custo_bruto_hipotetico_rs'])-int(r['depreciacao_acumulada_hipotetica_rs'])==int(r['valor_liquido_rs'])
  # O gabarito é segregado: a base pública não contém rótulos de anomalias.
assert counts['linhas']==len(ids)==500000
assert sums['DIREITO_USO_ARRENDAMENTO']==140111000
assert sums['IMOBILIZADO_OPERACAO']==25430247000
assert sum(sums.values())==25570358000
r={'status':'PASSOU','linhas':counts['linhas'],'ids_unicos':len(ids),'saldos_rs':dict(sums),'alertas_plantados_por_tipo':'consultar gabarito separado; não disponível na base cega','documentos_repetidos':sum(x>1 for x in docs.values()),'sha256_gzip':hashlib.sha256(p.read_bytes()).hexdigest(),'ressalva':'A base V2 é a população principal e não possui coluna de alertas; gabarito segregado.'}
(root/'resultados'/'QA_GERADOR_V2.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,ensure_ascii=False))
