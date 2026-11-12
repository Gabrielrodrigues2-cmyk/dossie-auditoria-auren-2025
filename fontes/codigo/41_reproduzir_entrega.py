#!/usr/bin/env python3
"""One command: V2 historical tests, V3 enhancement tests, reconciliation workbook and PDF academic annex.
No pretend reproduction of old main PDF: 130-page original is preserved and annex is concatenated.
"""
import subprocess,sys,pathlib
root=pathlib.Path(__file__).resolve().parent.parent
for s in ['22_executar_verificacoes.py','40_testes_integrados_checklist.py','43_conciliar_resultado_administracao.py','39_criar_planilha_analitica.py','42_anexo_substantivo_pdf.py']:
 p=subprocess.run([sys.executable,str(root/'codigo'/s)],cwd=root)
 if p.returncode:raise SystemExit(f'FAIL: {s}: {p.returncode}')
print('PASSOU -- conferir resultados/QA_CHECKLIST_25OUT.json; dossie/DOSSIE_AUREN_2025_REVISAO_CHECKLIST.pdf')
