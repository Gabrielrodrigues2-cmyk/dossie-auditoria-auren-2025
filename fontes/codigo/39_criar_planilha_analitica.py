#!/usr/bin/env python3
"""Workbook of public-PDF extracted accounts, reconciliation and Note15b graph."""
try:
 from artifact_tool import Workbook,SpreadsheetFile
except ImportError:
 print('AVISO: artifact_tool não instalado. O CSV auditável foi produzido pela etapa 37; planilha XLSX pronta continua incluída no pacote. Para REGERAR a planilha, usar ambiente com artifact_tool.')
 raise SystemExit(0)
import csv,json,pathlib
root=pathlib.Path(__file__).resolve().parent.parent;O=root/'planilhas';O.mkdir(exist_ok=True)
with (root/'analises/DFP_2025_2024_EXTRAIDA_PDF_BP_DRE_DFC.csv').open(encoding='utf-8-sig') as f:rows=list(csv.DictReader(f))
with (root/'analises/NOTA15B_PERFIL_VENCIMENTO_DFP_2025.csv').open(encoding='utf-8-sig') as f:debt=list(csv.DictReader(f))
w=Workbook.create();s=w.worksheets.add('DFP_2025_2024')
s.get_range('A1:I1').values=[['Escopo','Demonstração','Código','Descrição','2025 R$ mil','2024 R$ mil','Var R$ mil','Página PDF','Fonte']]
values=[[r['escopo'],r['demonstracao'],r['codigo_conta_CVM'],r['descricao'],int(r['2025_RSmil']),int(r['2024_RSmil']),None,int(r['pagina_fisica_PDF']),'DFP 2025 V1'] for r in rows]
s.get_range(f'A2:I{len(rows)+1}').values=values
s.get_range('G2').formulas=[['=E2-F2']]
s.get_range(f'G2:G{len(rows)+1}').fill_down()
s.get_range('A1:I1').format.fill='#1E3350';s.get_range('A1:I1').format.font.color='#FFFFFF';s.get_range('A1:I1').format.font.bold=True
s.freeze_panes.freeze_rows(1)
s.get_range('D:D').format.column_width=53
s.get_range('A:A').format.column_width=19
s.get_range('B:B').format.column_width=16
s.get_range('C:C').format.column_width=18
s.get_range('E:G').format.column_width=19
s.get_range('H:I').format.column_width=17
s.get_range(f'E2:G{len(rows)+1}').set_number_format('#,##0;[Red](#,##0)')
d=w.worksheets.add('Nota15b_Divida')
d.get_range('A1:E1').values=[['Ano','Fomento (R$ mil)','Debêntures (R$ mil)','Total (R$ mil)','Conferência diferença']]
for k,row in enumerate(debt,2):
 d.get_range(f'A{k}:C{k}').values=[[row['ano'],int(row['agencia_fomento_RSmil']),int(row['debentures_RSmil'])]]
 d.get_range(f'D{k}').formulas=[[f'=B{k}+C{k}']]
 d.get_range(f'E{k}').formulas=[[f'=D{k}-{int(row["total_RSmil"])}']]
d.get_range('A9').values=[['TOTAL']];d.get_range('B9').formulas=[['=SUM(B2:B8)']];d.get_range('C9').formulas=[['=SUM(C2:C8)']];d.get_range('D9').formulas=[['=SUM(D2:D8)']]
d.get_range('A1:E1').format.fill='#1E3350';d.get_range('A1:E1').format.font.color='#FFFFFF';d.get_range('A1:E1').format.font.bold=True
d.get_range('A:E').format.column_width=22
d.get_range('A11').values=[['Nota: dívida inclui amortização e JUROS PROJETADOS; não equivale ao saldo contábil do passivo.']]
d.get_range('A12').values=[['Fonte: DFP Auren FY2025, Nota 15(b), PDF físico p.106 / impresso p.105.']]
n=w.worksheets.add('Nota13a_V3')
n.get_range('A1:D1').values=[['Componente','DFP 2025 R$','V3 Sintética R$','Diferença R$']]
items=[('Custo bruto',42273221000),('Depreciação acumulada (dedução)',-17822049000),('Mais-valia PPA',1230019000),('Amortização PPA (dedução)',-250944000)]
for ix,(name,val) in enumerate(items,2):
 n.get_range(f'A{ix}:C{ix}').values=[[name,val,val]]
 n.get_range(f'D{ix}').formulas=[[f'=B{ix}-C{ix}']]
n.get_range('A6').values=[['Imobilizado operacional líquido']]
n.get_range('B6').formulas=[['=SUM(B2:B5)']];n.get_range('C6').formulas=[['=SUM(C2:C5)']];n.get_range('D6').formulas=[['=B6-C6']]
n.get_range('A7:C7').values=[['Direito de uso (líquido)',140111000,140111000]];n.get_range('D7').formulas=[['=B7-C7']]
n.get_range('A8').values=[['Imobilizado total']];n.get_range('B8').formulas=[['=B6+B7']];n.get_range('C8').formulas=[['=C6+C7']];n.get_range('D8').formulas=[['=B8-C8']]
n.get_range('A1:D1').format.fill='#1E3350';n.get_range('A1:D1').format.font.color='#FFFFFF';n.get_range('A1:D1').format.font.bold=True;n.get_range('A:D').format.column_width=28
n.get_range('A10').values=[['V3 é ficcional; igualdade agregada é CALIBRAÇÃO INTENCIONAL, não confirmação de lançamentos reais.']]

m=w.worksheets.add('Resultado_Admin_vs_DRE')
m.get_range('A1:G1').values=[['Ano','Admin R$ milhões','DRE R$ milhões','Diferença R$ milhões','Status','Página relatório','Página DRE']]
m.get_range('A2:C3').values=[[2025,-557.9,-557.875],[2024,271.9,271.869]]
for row in [2,3]:
 m.get_range(f'D{row}').formulas=[[f'=B{row}-C{row}']]
 m.get_range(f'E{row}').formulas=[[f'=IF(ROUND(C{row},1)=B{row},"COINCIDE ARREDONDAMENTO","REVISAR")']]
 m.get_range(f'F{row}:G{row}').values=[[59,19]]
m.get_range('A1:G1').format.fill='#1E3350';m.get_range('A1:G1').format.font.color='#FFFFFF';m.get_range('A1:G1').format.font.bold=True
m.get_range('A:G').format.column_width=25
m.get_range('A5').values=[['Relatório Administração na DFP física p59; DRE consolidada na p19, código 3.11.']]

p=O/'DFP_REAL_E_CONCILIACOES_V3.xlsx';SpreadsheetFile.export_xlsx(w).save(str(p));print('WORKBOOK',p, p.stat().st_size)
