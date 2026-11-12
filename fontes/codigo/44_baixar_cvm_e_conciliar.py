#!/usr/bin/env python3
"""Cotejo comprovado DFP PDF x CSV oficial CVM para Auren 2025/2024.
Usa ZIP CVM original; compara apenas versão máxima, exercício adequado e código.
Não deduz erro contábil de ausência de conta ou diferença de escopo.
"""
from pathlib import Path
from decimal import Decimal, InvalidOperation
from collections import Counter,defaultdict
import csv,io,zipfile,json,hashlib,urllib.request,sys
BASE=Path(__file__).resolve().parents[1]
URL='https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2025.zip'
ZIP=BASE/'fontes/cvm/dfp_cia_aberta_2025.zip'
OUT=BASE/'analises'
CNPJ='28594234000123'
TYPES={'BPA':'BP','BPP':'BP','DRE':'DRE','DFC_MI':'DFC'}
def normcnpj(v):return ''.join(c for c in str(v) if c.isdigit())
def dec(v):
 v=str(v or '').strip()
 if not v:return None
 try:return Decimal(v.replace('.','').replace(',','.')) if ',' in v else Decimal(v)
 except InvalidOperation:return None
def write_csv(path,rows,fields):
 with path.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
def run():
 if not ZIP.exists():
  ZIP.parent.mkdir(parents=True,exist_ok=True)
  with urllib.request.urlopen(URL,timeout=60) as r:ZIP.write_bytes(r.read())
 assert zipfile.is_zipfile(ZIP),'Arquivo CVM não é ZIP válido'
 sources=[];allrows=[]
 with zipfile.ZipFile(ZIP) as z:
  for typ,dt in TYPES.items():
   for suffix,scope in [('con','CONSOLIDADO'),('ind','CONTROLADORA')]:
    name=f'dfp_cia_aberta_{typ}_{suffix}_2025.csv'
    if name not in z.namelist():raise ValueError('Não há '+name)
    content=z.read(name).decode('cp1252')
    rows=[r for r in csv.DictReader(io.StringIO(content),delimiter=';') if normcnpj(r.get('CNPJ_CIA'))==CNPJ and r.get('DT_REFER')=='2025-12-31']
    if not rows:raise ValueError('Nenhum registro da Auren em '+name)
    version=max(int(r['VERSAO']) for r in rows)
    rows=[r for r in rows if int(r['VERSAO'])==version]
    sources.append({'arquivo':name,'versao_CVM':version,'linhas_ambos_exercicios':len(rows)})
    for r in rows:
     year={'ÚLTIMO':2025,'PENÚLTIMO':2024}.get(r['ORDEM_EXERC'])
     if not year:continue
     amount=dec(r['VL_CONTA'])
     if amount is None:continue
     # Arquivos DFP registram a unidade em ESCALA_MOEDA, que é MIL.
     if r['ESCALA_MOEDA'].strip().upper()=='UNIDADE':amount/=1000
     allrows.append({'escopo':scope,'demonstracao':dt,'codigo_conta_CVM':r['CD_CONTA'],'descricao_CVM':r['DS_CONTA'],'ano':year,'valor_cvm_RSmil':str(amount),'arquivo_origem':name,'versao':version,'escala':r['ESCALA_MOEDA']})
 pdf_path=OUT/'DFP_2025_2024_EXTRAIDA_PDF_BP_DRE_DFC.csv'
 with pdf_path.open(encoding='utf-8-sig',newline='') as f: pdf=list(csv.DictReader(f))
 mapping=defaultdict(list)
 for r in allrows:mapping[(r['escopo'],r['demonstracao'],r['codigo_conta_CVM'],r['ano'])].append(r)
 joined=[]
 for p in pdf:
  for year in (2025,2024):
   key=(p['escopo'],p['demonstracao'],p['codigo_conta_CVM'],year)
   found=mapping.get(key,[])
   vals={dec(r['valor_cvm_RSmil']) for r in found}
   pv=dec(p[f'{year}_RSmil'])
   if not found:status='SEM_CORRESPONDENCIA'
   elif len(vals)>1:status='VALORES_MULTIPLOS'
   elif pv==next(iter(vals)):status='CONCILIADO'
   else:status='DIVERGENTE'
   cv=next(iter(vals)) if len(vals)==1 else None
   joined.append({'escopo':p['escopo'],'demonstracao':p['demonstracao'],'ano':year,'codigo_conta':p['codigo_conta_CVM'],'descricao_PDF':p['descricao'],'valor_PDF_RSmil':str(pv) if pv is not None else '', 'valor_CVM_RSmil':str(cv) if cv is not None else '', 'diferenca_RSmil':str(pv-cv) if pv is not None and cv is not None else '', 'status':status,'pagina_fisica_PDF':p['pagina_fisica_PDF'],'arquivo_CVM':found[0]['arquivo_origem'] if found else ''})
 OUT.mkdir(exist_ok=True)
 write_csv(OUT/'CVM_AUREN_2025_2024_EXTRAIDA.csv',allrows,list(allrows[0]))
 write_csv(OUT/'COTEJO_PDF_VS_CVM_2025_2024.csv',joined,list(joined[0]))
 counts=Counter(x['status'] for x in joined)
 byscope=Counter((x['status'],x['escopo'],x['demonstracao'],x['ano']) for x in joined)
 report={'fonte_oficial':URL,'arquivo_recebido':str(ZIP.relative_to(BASE)),'sha256_zip':hashlib.sha256(ZIP.read_bytes()).hexdigest(),'cnpj_auren':'28.594.234/0001-23','data_referencia':'2025-12-31','linhas_CVM_ambos_anos':len(allrows),'contas_PDF':len(pdf),'comparacoes_anuais':len(joined),'status':dict(counts),'detalhe_por_escopo_demonstracao_ano':[{'status':s,'escopo':e,'demonstracao':d,'ano':y,'quantidade':n} for (s,e,d,y),n in sorted(byscope.items())],'fontes':sources,'metodologia':'Correspondência por escopo, demonstração, código de conta e exercício; selecionada última versão da DFP 2025 da CVM. Valores em R$ mil.','limites':'Extração de contas do PDF pré-existente; confrontos textuais e notas explicativas não estão abrangidos. Diferenças não comprovam erros contábeis.'}
 (OUT/'RESULTADO_COTEJO_CVM.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({k:report[k] for k in ('linhas_CVM_ambos_anos','contas_PDF','comparacoes_anuais','status')},ensure_ascii=False,indent=2))
 return report
if __name__=='__main__':
 try:run()
 except Exception as exc:print('ERRO:',repr(exc),file=sys.stderr);sys.exit(2)
