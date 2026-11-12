#!/usr/bin/env python3
"""PT 600: reproducible DIDACTIC materiality allocations by disclosed segments, DFP physical p78, NOT legal entity materialities.
All amounts are R$ thousands. Never represent group engagement actual instructions or component audits.
"""
import csv, json, pathlib,hashlib
R=pathlib.Path(__file__).resolve().parents[1]; OUT=R/'analises';OUT.mkdir(exist_ok=True)
assets_consolidated=48727388
materiality_group=round(assets_consolidated*.005,3)
performance_group=round(materiality_group*.7,3)
trivial_group=round(materiality_group*.05,3)
# Public Note 4, 2025, PDF physical page 78, all R$ x 1000.
segments=[
 {'grupo':'SEG_GERACAO','nome':'Geração','receita_2025':6556105,'resultado_operacional_2025':1995913,'eliminacoes_receita_2025':0,'base':'receita do segmento','fator':.005,'conta_base':6556105,'risco':'alto: ativos de geração, impairment, curtailment, contratos e PPA','teste':'PPE impairment, concessões, estimativas e integridade geração'},
 {'grupo':'SEG_COMERCIALIZACAO','nome':'Comercialização','receita_2025':9244401,'resultado_operacional_2025':475007,'eliminacoes_receita_2025':0,'base':'receita do segmento','fator':.005,'conta_base':9244401,'risco':'alto: preço de contratos, derivativos, corte de receita, CCEE','teste':'reconciliação contratos/CCEE, mensuração PPA, operações com relacionadas'},
 {'grupo':'SEG_HOLDING','nome':'Holding e Pipelines','receita_2025':0,'resultado_operacional_2025':-220331,'eliminacoes_receita_2025':0,'base':'valor absoluto do prejuízo operacional segmentado','fator':.03,'conta_base':220331,'risco':'alto: financiamento, tributos diferidos, projetos em implantação, garantias','teste':'empréstimos, covenants, tributos diferidos, projetos e partes relacionadas'},
 {'grupo':'AJUSTES_CONSOLIDACAO','nome':'Ajustes e eliminações','receita_2025':-2623554,'resultado_operacional_2025':139812,'eliminacoes_receita_2025':-2623554,'base':'valor absoluto da eliminação da receita','fator':.0025,'conta_base':2623554,'risco':'alto: transações intercompanhias, alocação e eliminação','teste':'reexecução de eliminações e reconciliação saldos intercompanhias'},
]
assert sum(s['receita_2025'] for s in segments)==13176952
# Nota: resultado operacional extraído do PDF por texto NÃO fecha neste cruzamento; não tratar como conciliação de lucros.
for s in segments:
 s['materialidade_segmento_proposta_mil']=round(s['conta_base']*s['fator'],3)
 s['materialidade_execucao_segmento_proposta_mil']=round(s['materialidade_segmento_proposta_mil']*.7,3)
 s['status']='SD_PLANEJAMENTO_EX_ANTE_NAO_ATRIBUIDA_A_ENTIDADE_JURIDICA'
 s['fonte']='DFP 2025 Nota 4 p. física 78; BP consolidado p. física 15'
 assert 0 < s['materialidade_segmento_proposta_mil'] < materiality_group
assert sum(s['materialidade_segmento_proposta_mil'] for s in segments)<performance_group
p=OUT/'PT600_MATERIALIDADE_SEGMENTOS_PUBLICOS_2025.csv'
with p.open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(segments[0].keys()));w.writeheader();w.writerows(segments)
report={'natureza':'SD planejamento didático com números de segmentos RP; não é materialidade aprovada pelo auditor do grupo','fonte':'DFP Auren 2025, Nota 4, página física 78, e BP consolidado, página física 15','unidade':'R$ milhares','ativo_consolidado':assets_consolidated,'materialidade_global_proposta':materiality_group,'materialidade_execucao_global_proposta':performance_group,'limite_trivial_global_proposto':trivial_group,'receita_por_segmentos_mais_eliminacoes':sum(x['receita_2025'] for x in segments),'receita_consolidada_dfp':13176952,'resultado_operacional_segmentos_mais_ajustes':sum(x['resultado_operacional_2025'] for x in segments),'resultado_operacional_consolidado_extraido':2110777,'diferenca_resultado_operacional_sem_conciliacao':sum(x['resultado_operacional_2025'] for x in segments)-2110777,'ressalva_resultado_operacional':'A coluna de resultado operacional não fecha na extração textual; não afirmar reconciliação desse subtotal até inspeção gráfica e reconciliação independente','limiares_por_cluster':{s['grupo']:s['materialidade_segmento_proposta_mil'] for s in segments},'soma_limiares':round(sum(s['materialidade_segmento_proposta_mil'] for s in segments),3),'soma_menor_que_performance_global':True,'limitacoes':['segmentos operacionais são agrupamentos públicos e não equivalem necessariamente a componentes jurídicos para a NBC TA 600','benchmarks e percentuais são julgamento didático ilustrativo, não norma CFC nem orientação da PwC','não inferir ativos/receitas por pessoa jurídica nem atestar competência de auditores de componentes','uma vez identificadas entidades e pacotes reais, materialidade por componente deve ser recalculada com riscos específicos, agregação e decisão do auditor de grupo','a soma dos quatro limiares não prova que o risco agregado está aceitável; a restrição por soma é salvaguarda didática adicional'], 'adicionais_PA':['obter balancetes e consolidação por entidade em 31/12/2025','definir componentes reais significativos e selecionar trabalho','avaliar identificação de riscos específicos, incluindo receitas e eliminação','definir e comunicar materialidade de componente, limiar de reporte e testes','executar controle de qualidade e revisão dos auditores de componentes']}
(OUT/'PT600_ESPECIFICACAO_DE_ESCOPO_E_LIMITES.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'materialidade_global_mil':materiality_group,'soma_limiares_mil':report['soma_limiares'],'receita_conciliada':report['receita_por_segmentos_mais_eliminacoes']},ensure_ascii=False))
