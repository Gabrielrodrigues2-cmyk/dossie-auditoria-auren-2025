#!/usr/bin/env python3
"""Teste de integridade da convenção de versão V3; somente leitura; não emite asseguração."""
from pathlib import Path
import csv,gzip,json,hashlib,re,sys
R=Path(__file__).resolve().parents[1]
V3='dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz'
V2='dados_sinteticos_v2/imobilizado_500000_v2_REGERADO.csv.gz'
assert (R/V3).exists() and (R/V2).exists()
assert (R/'documentacao/DICIONARIO_V3.md').exists()
assert 'V3' in (R/'README.md').read_text()
assert 'V2 (somente acervo histórico)' in (R/'README.md').read_text()
pts=list((R/'PT').glob('PT_*.md'));assert len(pts)==27
for p in pts:
 s=p.read_text(encoding='utf8')
 assert ('BASE SINTÉTICA PRINCIPAL [SD]:** **V3**' in s or 'V3 PRINCIPAL' in s),p
 assert not re.search(r'^\*\*REFERÊNCIA DA POPULAÇÃO SINTÉTICA OFICIAL \(SD\):\*\* V2',s,re.M),p
for p in (R/'programas').glob('*.md'):
 assert 'V3 é a base principal' in p.read_text(encoding='utf8'),p
with gzip.open(R/V3,'rt',encoding='utf8',newline='') as f:
 rd=csv.DictReader(f); assert 'alertas' not in rd.fieldnames; n=0; IDs=set()
 for row in rd:
  n+=1;IDs.add(row['id_ativo'])
assert len(IDs)==n==500000,(n,len(IDs))
r=json.loads((R/'analises/PT530_V3_PLANO_E_RESULTADOS.json').read_text())
assert r['base_primaria']=='V3' and r['n']==600 and r['itens_certeza']==40
assert [x['desvios_detectaveis_observados'] for x in r['estratos']]==[0,1]
assert r['estratos'][0]['limite_superior_unilateral_95_CP']<.02<r['estratos'][1]['limite_superior_unilateral_95_CP']
assert sum(1 for _ in csv.DictReader((R/'analises/PT530_V3_AMOSTRA_E_TESTES_600.csv').open()))==600
assert sum(1 for _ in csv.DictReader((R/'analises/PT530_V3_ITENS_CERTEZA_40.csv').open()))==40
for mandatory in ['analises/PT530_V3_INTERVALOS_E_DECISAO.csv','dados_sinteticos_v3/CONCILIACAO_V3.json','documentacao/PROTOCOLO_VERSIONAMENTO_V3_2026.md']:
 assert (R/mandatory).exists()
report={'status':'PASSOU','versao_principal':'V3','v2':'HISTORICO','pt':len(pts),'populacao_v3':n,'n_amostra_v3':r['n'],'itens_certeza_v3':r['itens_certeza'],'intervalos_95':[round(x['limite_superior_unilateral_95_CP'],6) for x in r['estratos']],'limite':'Dados sintéticos e documentação; não asseguração sobre Auren'}
print(json.dumps(report,ensure_ascii=False,indent=2))
