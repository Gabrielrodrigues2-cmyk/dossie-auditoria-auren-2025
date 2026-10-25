#!/usr/bin/env python3
"""Procedimentos didáticos V2 independentes, sem acesso à companhia. Python padrão."""
import csv,gzip,random,collections,json,pathlib,hashlib
ROOT=pathlib.Path(__file__).resolve().parent.parent
SRC=ROOT/'dados_sinteticos_v2'/'imobilizado_500000_v2_REGERADO.csv.gz'
TRUTH=ROOT/'dados_sinteticos_v2'/'gabarito_v2_SEPARADO.csv'
OUT=ROOT/'analises';OUT.mkdir(exist_ok=True)
assert SRC.exists() and TRUTH.exists(), 'Execute primeiro codigo/26_gerar_base_v2.py --output dados_sinteticos_v2'
seed=20251023
by_scope=collections.defaultdict(list); seen=set(); total=collections.Counter(); alerts=collections.Counter(); flagged=set();doc_to_ids=collections.defaultdict(list)
with gzip.open(SRC,'rt',encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f):
  aid=r['id_ativo'];assert aid not in seen;seen.add(aid)
  by_scope[r['escopo_dfp_2025']].append(r)
  total[r['escopo_dfp_2025']]+=int(r['valor_liquido_rs'])
  # Não há coluna de alertas na população disponibilizada; sem rótulos na seleção.
  doc_to_ids[r['documento_sintetico']].append(aid)
assert len(seen)==500000
assert total['IMOBILIZADO_OPERACAO']==25430247000 and total['DIREITO_USO_ARRENDAMENTO']==140111000
# Seleção estratificada sem reposição, alocação proporcional arredondada: 597 + 3.
rng=random.Random(seed)
selected=[]; allocations={'IMOBILIZADO_OPERACAO':597,'DIREITO_USO_ARRENDAMENTO':3}
for scope in sorted(allocations):
 pool=by_scope[scope];sample=rng.sample(pool,allocations[scope]);selected.extend(sample)
selected.sort(key=lambda r:r['id_ativo'])
with (OUT/'PT530_V2_AMOSTRA_600_REPRODUZIVEL.csv').open('w',encoding='utf-8-sig',newline='') as f:
 fields=['id_ativo','escopo_dfp_2025','valor_liquido_rs','documento_sintetico','status_SD']
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in selected:w.writerow({k:r.get(k,'') if k!='status_SD' else 'DADO_FICTICIO' for k in fields})
truth=collections.defaultdict(set)
with TRUTH.open(encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f):truth[r['id_ativo']].add(r['anomalia_plantada'])
# Gabarito só é consultado DEPOIS da seleção e detecção; separado da população para avaliar recuperação.
truth_ids=set(truth)
# Critério de triagem no arquivo de amostra: duplicidade documental detectável em campos observáveis.
detected=set()
# Critério documental adicional: mesmo documento atribuído a IDs distintos.
duplicates={aid for aids in doc_to_ids.values() if len(aids)>1 for aid in aids}
detected |= duplicates
sample_ids={r['id_ativo'] for r in selected}
sample_truth=sample_ids & truth_ids
sample_detected=sample_ids & detected
report={'classificacao':'SD — população V2 sintética, não ativos da Auren','seed_amostra':seed,'populacao_total':len(seen),'alocacao_amostra':allocations,'amostra_total':len(selected),'saldo_2025_rs':dict(total),'anomalias_plantadas_registros_distintos':len(truth_ids),'ids_com_alerta_textual':'não aplicável: coluna removida da base pública','ids_documento_duplicado':len(duplicates),'ids_detectados_por_alerta_ou_documento_duplicado':len(detected),'ids_gabarito_e_detectados':len(truth_ids&detected),'ids_detectados_nao_gabarito':len(detected-truth_ids),'ids_gabarito_nao_detectados':len(truth_ids-detected),'amostra_com_anomalia_plantada':len(sample_truth),'amostra_com_alerta_ou_documento_duplicado':len(sample_detected),'amostra_com_alerta_e_gabarito':len(sample_truth&sample_detected),'anomalias_por_tipo':'consultar exclusivamente gabarito segregado','observacao':'A triagem deste script verifica exclusivamente duplicidade documental e não lê rótulos de plantio. Gabarito consultado depois da triagem. Não projetar taxa de erros contábeis para a Auren; não há evidência real. Amostra não demonstra nível estatístico de confiança sem modelo de risco e erro tolerável.'}
(OUT/'PT530_V2_RELATORIO_TESTES_REPRODUZIVEIS.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
