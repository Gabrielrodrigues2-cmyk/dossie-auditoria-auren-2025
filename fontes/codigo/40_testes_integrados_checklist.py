#!/usr/bin/env python3
"""Deterministic regression with re-generation and checks. All synthetic data remains DIDACTIC."""
import pathlib,subprocess,sys,json,csv,gzip,hashlib
root=pathlib.Path(__file__).resolve().parent.parent
run=['35_reconstruir_analitico_v3.py','36_gerar_razao_simulado_pt240.py','37_extrair_dados_reais_dfp.py','38_nota15_vencimentos.py']
checks={}
for script in run:
 proc=subprocess.run([sys.executable,str(root/'codigo'/script)],cwd=root,capture_output=True,text=True)
 checks[script]={'exit':proc.returncode,'stdout':proc.stdout.strip()[-300:],'stderr':proc.stderr.strip()[-300:]}
 if proc.returncode:raise RuntimeError(str(checks[script]))
v=json.loads((root/'dados_sinteticos_v3/CONCILIACAO_V3.json').read_text())
assert v['registros']==500000 and v['total_liquido']==25570358000
c=v['composicao_rs']; assert (c['IMOBILIZADO_OPERACAO_custo'],c['IMOBILIZADO_OPERACAO_dep'],c['IMOBILIZADO_OPERACAO_ppa'],c['IMOBILIZADO_OPERACAO_amort_ppa'])==(42273221000,17822049000,1230019000,250944000)
with gzip.open(root/'dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz','rt',encoding='utf-8') as f:
 r=csv.DictReader(f); assert 'anomalia_plantada' not in r.fieldnames and 'alertas' not in r.fieldnames
 ids=set()
 for line in r:
  assert line['id_ativo'] not in ids;ids.add(line['id_ativo'])
 assert len(ids)==500000
j=json.loads((root/'dados_sinteticos_v3/PT240_RESULTADOS.json').read_text());assert j['total_debitos_rs']==j['total_creditos_rs'] and j['linhas_razao']==12000
s=json.loads((root/'analises/DFP_EXTRACAO_CONTROLES.json').read_text());assert s['linhas']>=290
n=json.loads((root/'analises/NOTA15B_ANALISE.json').read_text());assert n['soma_fluxos_RSmil']==24521253
before=v['sha256_csv_gz'];after=hashlib.sha256((root/'dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz').read_bytes()).hexdigest();assert before==after
# Fixed, hard-coded regression digests established at validated 25/10/2026 run.
# Updating seeds, ordering or generator requires explicit acceptance of a NEW golden test fixture.
golden={
 'dados_sinteticos_v2/imobilizado_500000_v2_REGERADO.csv.gz':'bfd1bac748c246d0bd7768688a2816c1a2ca20116a804f678669973cbbf85971',
 'dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz':'3b378a2197cf4f95ad6d7ce80f7d9619db9d34e5d3f413ab473b76dbd8b40632',
 'dados_sinteticos_v3/RAZAO_PT240_12000_LINHAS.csv':'ce622a092cf150d135cbd515c93588287328fc3f853075fecb45a1ea21755fbd'
}
for filename,expected in golden.items():
 actual=hashlib.sha256((root/filename).read_bytes()).hexdigest()
 assert actual==expected,(filename,actual,expected)
report={'status':'PASSOU','base_v3':len(ids),'saldo_liquido_v3':v['total_liquido'],'razao_linhas':j['linhas_razao'],'dfp_linhas_pdf':s['linhas'],'perfil_divida_soma_RSmil':n['soma_fluxos_RSmil'],'sha256_goldens_passaram':True,'goldens':golden,'scripts':checks,'limite':'Não comprova integridade/validade dos dados internos da Auren nem vigência normativa.'}
(root/'resultados/QA_CHECKLIST_25OUT.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');print(json.dumps({k:report[k] for k in ['status','base_v3','razao_linhas','dfp_linhas_pdf']},ensure_ascii=False))
