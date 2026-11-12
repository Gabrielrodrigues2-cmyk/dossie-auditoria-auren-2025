#!/usr/bin/env python3
"""Check structural, data and PDF integrity. Run after pipeline: python codigo/32_validar_entrega.py"""
from pathlib import Path
import csv,gzip,hashlib,json,sys
from pypdf import PdfReader
R=Path(__file__).resolve().parent.parent
codes="EC 200 210 220 230 240 250 260 265 300 315 320 330 402 450 500 501 505 510 520 530 540 550 560 570 580 600".split()
missing=[str(p.relative_to(R)) for x in codes for p in [R/f'PT/PT_{x}.md',R/f'programas/PROGRAMA_PT_{x}.md'] if not p.is_file()]
assert not missing,missing
p=R/'dados_sinteticos_v2/imobilizado_500000_v2_REGERADO.csv.gz'
ids=set();totals={};cnt=0
with gzip.open(p,'rt',encoding='utf8') as f:
 reader=csv.DictReader(f)
 assert 'alertas' not in reader.fieldnames
 for row in reader:
  cnt+=1;ids.add(row['id_ativo']);scope=row['escopo_dfp_2025'];totals[scope]=totals.get(scope,0)+int(row['valor_liquido_rs'])
assert cnt==len(ids)==500000,(cnt,len(ids))
assert totals=={'DIREITO_USO_ARRENDAMENTO':140111000,'IMOBILIZADO_OPERACAO':25430247000},totals
result=json.loads((R/'analises/PT530_V2_TESTE_INDEPENDENTE_SEM_COLUNA_ALERTAS.json').read_text())
assert result['ids_detectados_sem_ler_alertas']==982
pdf=R/'dossie/DOSSIE_AUREN_2025_APROFUNDADO_FINAL.pdf'
pages=len(PdfReader(pdf).pages)
assert pages>=100,pages
from csv import DictReader
with (R/'documentacao/MATRIZ_RASTREABILIDADE_AVALIACAO.csv').open(encoding='utf-8-sig') as f:assert len(list(DictReader(f)))==27
result={'status':'PASSOU_CONTROLES_TECNICOS','pt':27,'registros':cnt,'ids_unicos':len(ids),'saldo_rs':sum(totals.values()),'ids_sinalizados':982,'paginas_pdf':pages,'sha256_pdf':hashlib.sha256(pdf.read_bytes()).hexdigest(),'nota':'Integridade técnica não certifica mérito, suficiência de evidência nem vigência de normas.'}
(R/'resultados/VALIDACAO_TECNICA_PARA_AVALIACAO_IA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False))
