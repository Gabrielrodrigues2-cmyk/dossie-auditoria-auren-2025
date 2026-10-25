#!/usr/bin/env python3
"""Pipeline oficial SD: geração V2 -> validação -> amostra -> detecção sem alertas -> conciliação DFP.
Requer Python 3. Execute: python codigo/22_executar_verificacoes.py
"""
from pathlib import Path
import subprocess,sys,json
root=Path(__file__).resolve().parent.parent
scripts=['26_gerar_base_v2.py','27_verificar_gerador_v2.py','28_pt530_v2_testes_reproduziveis.py','29_teste_independente_v2.py','13_conciliacao_nota13.py']
results=[]
for script in scripts:
 cmd=[sys.executable,str(root/'codigo'/script)]
 if script=='26_gerar_base_v2.py':cmd+=['--output','dados_sinteticos_v2']
 done=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
 results.append({'codigo':script,'retorno':done.returncode,'saida':done.stdout[-1200:],'erro':done.stderr[-1000:]})
 if done.returncode:raise RuntimeError(script+' FALHOU: '+done.stderr[-800:])
generation=json.loads((root/'dados_sinteticos_v2/RELATORIO_GERACAO_V2.json').read_text())
blind=json.loads((root/'analises/PT530_V2_TESTE_INDEPENDENTE_SEM_COLUNA_ALERTAS.json').read_text())
sample=json.loads((root/'analises/PT530_V2_RELATORIO_TESTES_REPRODUZIVEIS.json').read_text())
assert generation['registros']==500000 and blind['populacao']==500000 and sample['amostra_total']==600
assert blind['ids_detectados_sem_ler_alertas']==982
report={'status':'PASSOU','base_principal':'dados_sinteticos_v2/imobilizado_500000_v2_REGERADO.csv.gz','linhas':500000,'amostra':600,'deteccoes_sem_coluna_alertas':982,'comandos':results,'observacao':'SD, não evidencia de auditoria de ativos reais da Auren'}
(root/'resultados/QA_PIPELINE_PRINCIPAL_V2.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['status','base_principal','linhas','amostra','deteccoes_sem_coluna_alertas']},ensure_ascii=False))
