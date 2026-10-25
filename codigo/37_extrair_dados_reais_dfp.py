#!/usr/bin/env python3
"""Extracts printed statement rows from 2025 official DFP PDF (individual/consolidated; 2025/2024). Literal PDF evidence RP, never CVM open data comparison."""
import fitz,re,csv,pathlib,collections,json
ROOT=pathlib.Path(__file__).resolve().parent.parent
P=fitz.open(ROOT/'fontes/AUREN_DFP_2025.pdf');O=ROOT/'analises';O.mkdir(exist_ok=True)
num=re.compile(r'^[+-]?\d{1,3}(?:\.\d{3})*(?:,\d+)?$|^[+-]?\d+$')
code=re.compile(r'^[1-9](?:\.\d{2}){0,8}$')
rows=[]
for pg in range(2,29):
 t=P[pg].get_text('text').splitlines();title=t[0]
 if not (('Individuais' in title or 'Consolidadas' in title) and any(k in title for k in ['Balanço Patrimonial','Demonstração do Resultado','Demonstração do Fluxo de Caixa'])):continue
 scope='CONSOLIDADO' if 'Consolidadas' in title else 'CONTROLADORA'
 typ='BP' if 'Balanço Patrimonial' in title else 'DFC' if 'Fluxo de Caixa' in title else 'DRE' if 'Demonstração do Resultado' in title else 'OUTROS'
 if 'Abrangente' in title:continue
 for i,val in enumerate(t):
  if not code.fullmatch(val.strip()):continue
  if i+3>=len(t):continue
  label=t[i+1].strip()
  if not label or num.fullmatch(label) or len(label)>230:continue
  a,b=t[i+2].strip(),t[i+3].strip()
  if not(num.fullmatch(a) and num.fullmatch(b)):continue
  try:n25=int(a.replace('.',''));n24=int(b.replace('.',''))
  except:continue
  rows.append([scope,typ,val.strip(),label,n25,n24,n25-n24,pg+1,'DFP 2025, versão 1','R$ mil'])
# id unique; avoid false positives: accept systematic code order only
bykey={}
for r in rows:bykey[(r[0],r[1],r[2])]=r
rows=sorted(bykey.values(),key=lambda r:(r[0],r[1],r[2]))
with (O/'DFP_2025_2024_EXTRAIDA_PDF_BP_DRE_DFC.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['escopo','demonstracao','codigo_conta_CVM','descricao','2025_RSmil','2024_RSmil','variacao_RSmil','pagina_fisica_PDF','fonte','unidade']);w.writerows(rows)
report={'classificacao':'RP extração de texto do PDF público recebido; não é conciliação independente com base estruturada da CVM','linhas':len(rows),'escopos':dict(collections.Counter(f'{r[0]} {r[1]}' for r in rows)),'limite':'Não inclui DRA/DMPL/DVA; contas e descrições precisam de revisão visual se exigida exatidão célula a célula. Valores 2024 são coluna comparativa contida na DFP 2025.','controles':[]}
for scope in ['CONSOLIDADO','CONTROLADORA']:
 for typ,rootcode in [('BP','1'),('DRE','3.01'),('DFC','6.01')]:
  found=next((r for r in rows if r[0]==scope and r[1]==typ and r[2]==rootcode),None)
  if found:report['controles'].append({'escopo':scope,'demonstracao':typ,'codigo':rootcode,'valor_2025_RSmil':found[4],'valor_2024_RSmil':found[5],'pagina':found[7]})
(O/'DFP_EXTRACAO_CONTROLES.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'linhas':len(rows),'escopos':report['escopos']},ensure_ascii=False))
