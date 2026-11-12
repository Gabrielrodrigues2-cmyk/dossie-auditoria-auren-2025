#!/usr/bin/env python3
from pathlib import Path
import csv,json,gzip,math,hashlib,sys
R=Path(__file__).resolve().parents[1]
P=R/'PT';A=R/'analises';D=R/'documentacao'
pts=list(P.glob('PT_*.md'))
assert len(pts)==27, f'PT={len(pts)}'
for p in pts:
 t=p.read_text(encoding='utf-8');assert '**BASE SINTÉTICA PRINCIPAL [SD]:** **V3**' in t or 'V3 PRINCIPAL' in t,p
assert 'Metodologia principal vigente' in (P/'PT_530.md').read_text()
assert 'RETIFICAÇÃO SUBSTANTIVA C2' in (P/'PT_600.md').read_text()
with gzip.open(R/'dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz','rt',encoding='utf-8',newline='') as f:
 rd=csv.DictReader(f);assert 'alertas' not in rd.fieldnames;ids=set();n=0
 for row in rd:
  ids.add(row['id_ativo']);n+=1
assert n==len(ids)==500000,(n,len(ids))
r=json.loads((A/'PT530_V3_PLANO_E_RESULTADOS.json').read_text())
assert r['n']==600 and r['itens_certeza']==40
assert len(r['estratos'])==2
assert [x['desvios_detectaveis_observados'] for x in r['estratos']]==[0,1]
assert r['estratos'][0]['limite_superior_unilateral_95_CP']<.02<r['estratos'][1]['limite_superior_unilateral_95_CP']
with (A/'PT530_V3_AMOSTRA_E_TESTES_600.csv').open(encoding='utf-8') as f:assert sum(1 for _ in csv.DictReader(f))==600
with (A/'PT530_V3_ITENS_CERTEZA_40.csv').open(encoding='utf-8') as f:assert sum(1 for _ in csv.DictReader(f))==40
g=json.loads((A/'PT600_ESPECIFICACAO_DE_ESCOPO_E_LIMITES.json').read_text())
assert g['receita_por_segmentos_mais_eliminacoes']==g['receita_consolidada_dfp']==13176952
assert g['soma_limiares']<g['materialidade_execucao_global_proposta']
with (D/'MATRIZ_CORRECOES_PROFESSOR_2026.csv').open(encoding='utf-8-sig') as f:
 rr=list(csv.DictReader(f));assert len(rr)==7
 for row in rr:
  for name in row['arquivos_evidencia'].split('; '):assert (R/name).exists(),name
print(json.dumps({'status':'PASSOU','pt':27,'base_v3_linhas':n,'amostra_v3':600,'certeza':40,'receita_segmentos_mil':13176952,'criterios':7},ensure_ascii=False))
