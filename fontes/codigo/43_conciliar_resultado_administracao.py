#!/usr/bin/env python3
"""Compare visually verified Auren management report net income to DFP formal consolidated DRE."""
from pathlib import Path
import csv,json
root=Path(__file__).resolve().parent.parent
src=root/'analises/DFP_2025_2024_EXTRAIDA_PDF_BP_DRE_DFC.csv'
with src.open(encoding='utf-8-sig') as f:rows=list(csv.DictReader(f))
dre=[r for r in rows if r['escopo']=='CONSOLIDADO' and r['demonstracao']=='DRE' and r['codigo_conta_CVM']=='3.11']
assert len(dre)==1
row=dre[0]
# Management report PDF physical page 59, printed page 58, displays R$ millions to one decimal.
res=[]
for year,reported in [('2025',-557.9),('2024',271.9)]:
 actual=int(row[f'{year}_RSmil'])
 exact=actual/1000
 assert round(exact,1)==reported
 res.append({'exercicio':year,'relatorio_administracao_RSmilhoes_1_decimal':reported,'DRE_consolidada_RSmilhoes':exact,'diferenca_arredondamento_RSmilhoes':round(reported-exact,3),'conclusao':'COINCIDE por arredondamento a 1 casa decimal','pagina_relatorio_administracao_pdf':59,'pagina_DRE_pdf':19})
with (root/'analises/RECONCILIACAO_RESULTADO_ADMIN_DRE.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(res[0]));w.writeheader();w.writerows(res)
(root/'analises/RECONCILIACAO_RESULTADO_ADMIN_DRE.json').write_text(json.dumps({'fonte':'DFP Auren 2025, Relatório Administração PDF físico p.59 (impresso 58) e DRE PDF físico p.19 (impresso 18)','comparacao':res,'caveat':'R$ milhões arredondados a uma casa decimal na administração; conciliação documental textual+visual, não validação independente de resultado contábil'},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(res,ensure_ascii=False))
