#!/usr/bin/env python3
"""Journal entries are synthetic: balanced, deterministically generated, with distinct truth ledger and blind indicator detection."""
import csv,random,pathlib,collections,json,hashlib
ROOT=pathlib.Path(__file__).resolve().parent.parent
O=ROOT/'dados_sinteticos_v3';O.mkdir(exist_ok=True)
rng=random.Random(20251025); entries=O/'RAZAO_PT240_12000_LINHAS.csv';truth=O/'GABARITO_LANCAMENTOS_PT240.csv'
ledger=[];truth_rows=[]
for i in range(6000):
 amt=rng.randint(100,850000); date=f'2025-{rng.randint(1,12):02d}-{rng.randint(1,28):02d}'
 user=f'USR{rng.randint(1,18):02d}'; description=rng.choice(['Folha sintética','Imobilizado sintético','Energia sintética','Fornecedor sintético','Ajuste simulado'])
 if i%491==0: amt=500000;user='ADMIN99';truth_rows.append((f'V3-LAN-{i+1:06d}','USUARIO_PRIVILEGIADO_E_VALOR_REDONDO'))
 if i%733==0:date='2025-12-31';description='Ajuste manual fechamento';truth_rows.append((f'V3-LAN-{i+1:06d}','AJUSTE_FECHAMENTO'))
 jid=f'V3-LAN-{i+1:06d}'
 pair=rng.choice([('1.02.03-Imobilizado','2.01.01-Fornecedores'),('3.01-Custos','1.01.01-Caixa'),('1.01.02-Clientes','3.01-Receita'),('3.02-Despesa','2.01.02-Provisoes')])
 for typ,acc in [('D',pair[0]),('C',pair[1])]:ledger.append([jid,date,user,acc,typ,amt,description])
with entries.open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['id_lancamento','data','usuario','conta_sintetica','natureza_DC','valor_rs','descricao']);w.writerows(ledger)
with truth.open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['id_lancamento','motivo_plantado']);w.writerows(truth_rows)
assert len(ledger)==12000
# Rule-based detection does not reference ground-truth before classification.
reasons=collections.defaultdict(list);debit=credit=0
for row in ledger:
 jid,dt,user,account,typ,amt,desc=row
 if typ=='D':debit+=amt
 else:credit+=amt
 if user=='ADMIN99' and amt%100000==0:reasons[jid].append('USUARIO_PRIVILEGIADO_VALOR_REDONDO')
 if dt=='2025-12-31' and 'Ajuste manual' in desc:reasons[jid].append('AJUSTE_FECHAMENTO')
assert debit==credit
with (O/'PT240_TRIAGEM_CEGA.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['id_lancamento','sinal_de_risco','interpretacao']);
 for id,flags in sorted(reasons.items()):w.writerow([id,';'.join(sorted(set(flags))),'FLAG_DE_RISCO_NAO_DISTORCAO_CONFIRMADA'])
ground={i for i,_ in truth_rows};detected=set(reasons)
rep={'classificacao':'SD','lancamentos':6000,'linhas_razao':len(ledger),'total_debitos_rs':debit,'total_creditos_rs':credit,'triagem_sem_gabarito':len(detected),'planted_distintos':len(ground),'verdadeiros_positivos_didaticos':len(ground&detected),'falsos_positivos_didaticos':len(detected-ground),'avisos':'Red flags didáticas não são prova de fraude; contas fictícias e nenhuma ligação a razão real da Auren','sha256':hashlib.sha256(entries.read_bytes()).hexdigest()}
(O/'PT240_RESULTADOS.json').write_text(json.dumps(rep,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');print(json.dumps(rep,ensure_ascii=False))
