#!/usr/bin/env python3
"""Pré-entrega, somente leitura: falha com código não-zero diante de dados incoerentes."""
import pathlib,csv,hashlib,gzip,json,ast,sys
R=pathlib.Path(__file__).resolve().parents[1]
P=['EC','200','210','220','230','240','250','260','265','300','315','320','330','402','450','500','501','505','510','520','530','540','550','560','570','580','600']
def ok(condition,label):
 if not condition:raise RuntimeError('FALHOU: '+label)
 print('OK:',label)
for n in P:
 ok((R/f'PT/PT_{n}.md').is_file() and (R/f'programas/PROGRAMA_PT_{n}.md').is_file(),f'PT {n} e programa')
ok(len(list((R/'dossie').glob('*.pdf')))==1,'PDF oficial único')
for version,filename in [('V2','dados_sinteticos_v2/imobilizado_500000_v2_REGERADO.csv.gz'),('V3','dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz')]:
 n=0;ids=set();s=0
 with gzip.open(R/filename,'rt',encoding='utf-8-sig',newline='') as f:
  reader=csv.DictReader(f);ok('alertas' not in reader.fieldnames,version+' cega')
  for row in reader:
   n+=1;ids.add(row['id_ativo']);s+=int(row['valor_liquido_rs'])
 ok(n==500000 and len(ids)==n,version+' quantidade e IDs únicos')
 ok(s==25570358000,version+' conciliação líquida sintética')
for p in (R/'codigo').glob('*.py'):ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
print('OK: sintaxe de todos os códigos')
with (R/'analises/COTEJO_PDF_VS_CVM_2025_2024.csv').open(encoding='utf-8-sig',newline='') as f:
 rows=list(csv.DictReader(f))
ok(len(rows)==596 and all(x.get('status')=='CONCILIADO' for x in rows),'596/596 linhas cotejadas na tabela registrada')
with (R/'documentacao/MATRIZ_COBERTURA_NORMAS_ATUALIZADA.csv').open(encoding='utf-8-sig',newline='') as f:
 matrix=list(csv.DictReader(f))
ok(len(matrix)==27,'matriz 27 linhas')
for x in matrix:
 for key in ['Papel de trabalho','Programa','Localizador no consolidado','Dossiê oficial']:ok((R/x[key]).is_file(),'referência da matriz '+x[key])
with (R/'documentacao/REGISTRO_FONTES_VERIFICADAS.csv').open(encoding='utf-8-sig',newline='') as f:
 for x in csv.DictReader(f):
  q=R/x['Caminho no pacote'];ok(q.is_file() and hashlib.sha256(q.read_bytes()).hexdigest()==x['SHA256 do documento'],'fonte '+q.name)
print('PREFLIGHT CONCLUÍDO: verificações estruturais e aritméticas, não asseguração sobre demonstrações reais.')
