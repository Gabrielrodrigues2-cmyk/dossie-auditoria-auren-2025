#!/usr/bin/env python3
"""Nova base sintética V2, independente do histórico, determinística e reproduzível.
Não altera a base histórica, os PT anteriores nem a amostra antiga.
"""
import argparse,csv,gzip,io,random,hashlib,json,pathlib
N=500_000
TARGETS=[('DIREITO_USO_ARRENDAMENTO',2720,140_111_000),('IMOBILIZADO_OPERACAO',497280,25_430_247_000)]
COLS=['id_ativo','escopo_dfp_2025','classe','data_aquisicao_original','data_inicio_depreciacao_hipotetica','vida_util_anos_original','vida_util_anos_modelada','custo_bruto_hipotetico_rs','depreciacao_acumulada_hipotetica_rs','valor_liquido_rs','despesa_depreciacao_2025_hipotetica_rs','documento_sintetico']
def create(folder):
 folder=pathlib.Path(folder);folder.mkdir(parents=True,exist_ok=True)
 path=folder/'imobilizado_500000_v2_REGERADO.csv.gz'
 truth=folder/'gabarito_v2_SEPARADO.csv'
 rng=random.Random(20251023)
 with open(truth,'w',newline='',encoding='utf-8') as ftruth, open(path,'wb') as raw:
  tw=csv.writer(ftruth);tw.writerow(['id_ativo','anomalia_plantada'])
  with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=6) as gz:
   with io.TextIOWrapper(gz,encoding='utf-8',newline='') as txt:
    w=csv.DictWriter(txt,fieldnames=COLS,lineterminator='\n');w.writeheader()
    idx=0; stats={}
    for scope,n,total in TARGETS:
     # deterministic weights; exact published NET total by last-row adjustment
     weights=[rng.randint(5,5000) for _ in range(n)]
     wsum=sum(weights)
     values=[max(1,total*x//wsum) for x in weights]
     values[-1]+=total-sum(values)
     assert sum(values)==total and min(values)>0
     for j,net in enumerate(values):
      idx+=1;aid=f'V2-ATV-{idx:07d}'
      life=rng.choice([15,20,25,30,40])
      startyear=rng.randint(2012,2025)
      date=f'{startyear}-{rng.randint(1,12):02d}-{rng.randint(1,28):02d}'
      flags=[]
      if idx%997==0:flags.append('SUPORTE_AUSENTE')
      if idx%1499==0:flags.append('AQUISICAO_APOS_FECHAMENTO');date='2026-01-12'
      if idx%1999==0:flags.append('VIDA_UTIL_INCOMUM');life=99
      if idx%2499==0:flags.append('DOCUMENTO_REPETIDO')
      for flag in flags:tw.writerow([aid,flag])
      doc=f'V2-DOC-{idx-1:07d}' if 'DOCUMENTO_REPETIDO' in flags else f'V2-DOC-{idx:07d}'
      accum=net*rng.randint(5,45)//100
      gross=net+accum
      expense=gross//life if startyear<=2025 else 0
      w.writerow(dict(id_ativo=aid,escopo_dfp_2025=scope,classe=scope,data_aquisicao_original=date,data_inicio_depreciacao_hipotetica=date,vida_util_anos_original=life,vida_util_anos_modelada=life,custo_bruto_hipotetico_rs=gross,depreciacao_acumulada_hipotetica_rs=accum,valor_liquido_rs=net,despesa_depreciacao_2025_hipotetica_rs=expense,documento_sintetico=doc))
     stats[scope]={'registros':n,'saldo_liquido_rs':total}
 report={'natureza':'SD: nova base V2 independente; NAO reconstrucao da base historica','seed':20251023,'registros':N,'valores_publicos_usados_apenas_para_calibracao':stats,'sha256_gzip':hashlib.sha256(path.read_bytes()).hexdigest(),'sha256_gabarito':hashlib.sha256(truth.read_bytes()).hexdigest()}
 (folder/'RELATORIO_GERACAO_V2.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',default='dados_sinteticos_v2');a=p.parse_args();create(a.output)
