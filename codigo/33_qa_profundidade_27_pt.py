from pathlib import Path
import csv,gzip,json,re
R=Path(__file__).resolve().parent.parent
expected="EC 200 210 220 230 240 250 260 265 300 315 320 330 402 450 500 501 505 510 520 530 540 550 560 570 580 600".split()
errors=[]
for code in expected:
 p=R/'PT'/f'PT_{code}.md'; t=p.read_text(encoding='utf8')
 for name,pat in [('objetivo',r'objetivo'),('evidencia',r'evid.ncia|fontes'),('conclusao',r'conclus.o'),('revisor',r'____'),('secao_especifica',r'Revisão substantiva específica')]:
  if not re.search(pat,t,re.I):errors.append(f'{code}:{name}')
 if not all(x in t for x in ('[RP]','[PA]','[SD]')):errors.append(f'{code}:modalidades')
p=R/'dados_sinteticos_v2/imobilizado_500000_v2_REGERADO.csv.gz'
with gzip.open(p,'rt') as f:cols=next(csv.reader(f))
assert 'alertas' not in cols
result={'pt':len(expected),'erros':errors,'base_cego_sem_alertas':True}
(R/'resultados/QA_PROFUNDIDADE_27_PT.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(result)
if errors:raise SystemExit(1)
