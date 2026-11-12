#!/usr/bin/env python3
"""Valida a estrutura final e o manifesto SHA-256, sem instalar bibliotecas externas."""
import csv, hashlib, pathlib, gzip, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
PIDS=['EC','200','210','220','230','240','250','260','265','300','315','320','330','402','450','500','501','505','510','520','530','540','550','560','570','580','600']
for pid in PIDS:
 for f in [f'PT/PT_{pid}.md',f'programas/PROGRAMA_PT_{pid}.md']:
  assert (ROOT/f).is_file(),f
assert len(list((ROOT/'dossie').glob('*.pdf')))==1
assert (ROOT/'dossie/DOSSIE_AUREN_2025_CORRIGIDO_APOS_AVALIACAO.pdf').is_file()
with gzip.open(ROOT/'dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz','rt',encoding='utf-8-sig',newline='') as f:
 r=csv.DictReader(f); assert len(r.fieldnames)==12 and 'alertas' not in r.fieldnames
 n=0; ids=set()
 for row in r:
  ids.add(row['id_ativo']);n+=1
 assert n==500000 and len(ids)==n,(n,len(ids))
with (ROOT/'documentacao/MATRIZ_COBERTURA_NORMAS_ATUALIZADA.csv').open(encoding='utf-8-sig',newline='') as f:
 rows=list(csv.DictReader(f));assert len(rows)==27
 for row in rows:
  for key in ['Papel de trabalho','Programa','Localizador no consolidado','Dossiê oficial']:
   assert (ROOT/row[key]).is_file(),row[key]
with (ROOT/'documentacao/REGISTRO_FONTES_VERIFICADAS.csv').open(encoding='utf-8-sig',newline='') as f:
 for row in csv.DictReader(f):
  path=ROOT/row['Caminho no pacote'];assert path.is_file(),path
  assert hashlib.sha256(path.read_bytes()).hexdigest()==row['SHA256 do documento']
with (ROOT/'MANIFESTO_SHA256_FINAL.csv').open(encoding='utf-8-sig',newline='') as f:
 for row in csv.DictReader(f):
  path=ROOT/row['caminho'];assert path.is_file(),path
  assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256'],row['caminho']
print('APROVADO: 27 PT, único PDF, 500.000 IDs V3, matriz 27/27, fontes e hashes.')
