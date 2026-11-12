#!/usr/bin/env python3
"""Build PDF appendix with substantive second-reading of all 27 PT and concatenate to existing dossier.
The original 130-page academic PDF is retained unchanged; this annex is a transparent addendum.
"""
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import cm
from xml.sax.saxutils import escape
from pathlib import Path
import fitz,json
R=Path(__file__).resolve().parent.parent; out=R/'dossie';out.mkdir(exist_ok=True)
annex=out/'ANEXO_CHECKLIST_E_SEGUNDA_LEITURA_27_PT.pdf'
base=out/'DOSSIE_AUREN_2025_APROFUNDADO_FINAL.pdf'
final=out/'DOSSIE_AUREN_2025_REVISAO_CHECKLIST.pdf'
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='SecA',fontName='Helvetica-Bold',fontSize=12,leading=15,spaceBefore=15,spaceAfter=6,textColor=colors.HexColor('#17345A')))
styles.add(ParagraphStyle(name='TxtA',fontSize=9,leading=13,spaceAfter=7,alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='SmallA',fontSize=8,leading=11,spaceAfter=5))
styles.add(ParagraphStyle(name='BigA',fontSize=17,leading=21,spaceAfter=14,textColor=colors.HexColor('#17345A')))
story=[]
def H(t):story.append(Paragraph(escape(t),styles['SecA']))
def P(t):story.append(Paragraph(escape(t),styles['TxtA']))
def T(headers,body):
 a=Table([headers]+body,repeatRows=1,colWidths=[3.9*cm,5.0*cm,7.2*cm],hAlign='LEFT')
 a.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#17345A')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTSIZE',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#C6CFDB')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F6F8FC')]),('BOTTOMPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7)]));story.append(a)

story.append(Paragraph('ADENDO DE AUDITORIA ACADÊMICA — CHECKLIST FINAL',styles['BigA']))
P('Auren Energia S.A. | exercício 2025 | 25 de outubro de 2026 | Matrícula 232037730 | PT EC e NBC TA. Este adendo é parte do dossiê acadêmico e registra procedimentos adicionais, reconciliações, limites e uma segunda leitura individual dos 27 papéis de trabalho. Natureza: RP = evidência pública efetivamente inspecionada; SD = dados simulados; PA = procedimentos planejados sem acesso interno. Não é opinião de auditoria independente.')
H('1. Comparação com o padrão ISA: evidência acima do volume')
P('A revisão acrescentou (i) tabela de 298 contas e linhas de BP, DRE e DFC, individuais e consolidados, comparando 2025 e 2024 e identificando a página física da DFP; (ii) teste aritmético do perfil de vencimento no gráfico da Nota 15(b); (iii) base V3 com 500 mil itens e componentes brutos da Nota 13(a) conciliados; (iv) razão fictício independente com 12 mil linhas balanceadas; (v) testes automatizados de reprodução; e (vi) quadro público separado das anomalias didáticas. A extração da DFP é textual e não substitui confronto com os CSV oficiais da CVM, cujo download não foi possível neste ambiente.')
H('1.1. Resultado líquido — Relatório da Administração × DRE')
P('O Relatório da Administração na DFP 2025, página física 59 (impressa 58), declara resultado líquido CONSOLIDADO de prejuízo de R$557,9 milhões em 2025 e lucro de R$271,9 milhões em 2024. Na DRE consolidada, página física 19, código 3.11, constam prejuízo de R$557.875 mil (R$557,875 milhões) e lucro de R$271.869 mil (R$271,869 milhões), respectivamente. Os valores COINCIDEM após arredondamento a uma casa decimal: diferenças respectivas de R$25 mil e R$31 mil, sem evidência de inconsistência documental nessa rubrica. Consulte analises/RECONCILIACAO_RESULTADO_ADMIN_DRE.csv. Não se deve confundir resultado líquido consolidado, EBITDA ajustado gerencial e resultado individual.')
H('1.2. Conferência das edições normativas no consolidado do professor')
P('O sumário físico p.2 do Consolidado Normas Aud1.pdf indica, por exemplo, NBC TA 220(R3), 315(R2), 540(R2), 600(R2), 240(R1) e 560(R1). A relação completa das 26 NBC TA mais Estrutura Conceitual, com a primeira página indicada no sumário, foi extraída para documentacao/INDICE_NORMAS_CONSOLIDADO_PROFESSOR.csv. Isso confirma o RÓTULO da versão do arquivo do professor, mas não demonstra automaticamente que cada item de todos os PT é semanticamente pertinente nem certifica a vigência legal por pesquisa independente em fonte oficial.')
H('2. Reconciliação integral da Nota 13(a) — V3, R$')
T(['Componente','DFP 2025', 'Base V3 fictícia'],[
 ['Custo bruto','42.273.221.000','42.273.221.000'],['Depreciação acumulada','(17.822.049.000)','(17.822.049.000)'],['Mais-valia PPA','1.230.019.000','1.230.019.000'],['Amortização PPA','(250.944.000)','(250.944.000)'],['Imobilizado operacional líquido','25.430.247.000','25.430.247.000'],['Direito de uso líquido','140.111.000','140.111.000'],['Total conjunto','25.570.358.000','25.570.358.000']])
P('Método: gerador determinístico 35_reconstruir_analitico_v3.py, semente 20251025; 497.280 itens de imobilizado operacional e 2.720 direitos de uso. Quarenta âncoras ficcionais concentram 62% do custo bruto operacional, enquanto os demais componentes são pulverizados, para representar a assimetria de uma geradora de energia. O ajuste dos agregados foi feito por construção; os valores individuais não provêm de cadastro contábil real. Os valores brutos dos direitos de uso são inteiramente modelados: somente o líquido de R$140.111.000 está ancorado na DFP. Arquivos: dados_sinteticos_v3/ e resultados/QA_CHECKLIST_25OUT.json.')
H('3. Nota 15(b): perfil de vencimentos — transcrição do gráfico')
T(['Ano','Agências de fomento (R$ mil)','Debêntures / total (R$ mil)'],[['2026','645.762','1.292.578 / 1.938.340'],['2027','465.833','1.247.735 / 1.713.568'],['2028','500.916','1.284.954 / 1.785.870'],['2029','529.754','2.123.343 / 2.653.097'],['2030','462.833','1.755.190 / 2.218.023'],['2031','443.724','1.862.477 / 2.306.201'],['2032+','3.136.883','8.769.271 / 11.906.154']])
P('Soma dos sete intervalos: R$24.521.253 mil. A parcela de 2032 em diante representa 48,55% dos fluxos identificados. O gráfico inclui amortizações e juros projetados, não podendo ser igualado à dívida reconhecida no balanço. Fonte: DFP 2025, página física 106 (impressa 105). Os CSV de valores e conferência estão em analises/NOTA15B_*.')
H('4. Notas 18 e 20: riscos de contratos e ressarcimentos')
P('Nota 18 (contratos futuros de energia): o quadro da DFP, página física 113, informa ativos totais de R$2.985.151 mil, passivos de R$2.666.928 mil e saldo líquido de R$318.223 mil em 2025; em 2024 o líquido era R$190.336 mil. A movimentação de 2025 fecha por R$190.336 + 621.300 de marcação a mercado - 493.413 de realização = R$318.223 mil. O tema exige avaliar curvas de preços, posições de compra e venda e premissas de mensuração a valor justo. A DFP permite conciliação aritmética [RP], mas os contratos, curvas independentes, modelos, confirmações e liquidações detalhadas permanecem [PA].')
P('Nota 20 (ressarcimentos): a tabela da página física 116 mostra provisão de ressarcimento de R$900.907 mil na parcela circulante de 2025 e R$688.480 mil na não circulante, somando R$1.589.387 mil. A movimentação inclui constituição/reversão, amortização e atualização monetária, com exposição regulatória descrita até a página 117. É incorreto reduzir o saldo total a R$900,9 milhões sem qualificar que se trata de parcela circulante. Para avaliar integridade, confrontar unidades geradoras, regras CCEE/ANEEL e estimativas de compensação: [PA]. A manifestação não vinculante da companhia em agosto de 2026 não prova registro de ativo em 2025.')
H('5. PT 240: razão fictício de lançamentos e burla de controles')
P('O arquivo RAZAO_PT240_12000_LINHAS.csv contém 6 mil partidas dobradas completas, sem uso de contas reais da Auren. Débitos e créditos acumulados são iguais a R$2.553.487.120. A triagem independente detectou 21 IDs com indicadores como usuário privilegiado e valores redondos ou ajustes no encerramento; o gabarito segregado também contém 21 IDs. Essa coincidência foi construída para fins didáticos e NÃO demonstra eficácia na detecção de fraude real. São red flags que exigiriam exames de autorização, documentos e logs de sistema [PA].')
H('6. PT 530: estatística, amostra e limites')
P('A amostra V2 preexistente é estratificada, 597 itens operacionais e 3 de direitos de uso, total de 600, e não amostragem monetária por unidade (MUS). Os 982 alertas automáticos correspondem a regras sobre a base sintética e não devem ser projetados como erros contábeis. Para um teste de atributos binomial de 150 itens selecionados adequadamente e ZERO desvios observados, o limite superior unilateral de 95% seria 1-(0,05)^(1/150) = aproximadamente 1,98%; trata-se de um cenário teórico e não de resultado executado. Uma MUS exigiria PPS, valor contábil da amostra, valor efetivamente auditado, distorção tolerável e fator de confiança. A ausência de comprovantes independentes impede informar limite superior monetário honesto. Ver documentacao/NOTA_METODOLOGICA_AMOSTRAGEM_25OUT.md.')
H('7. PT 265 e PT 450: assuntos públicos não equivalem a distorções')
P('O registro PT265_CADASTRO_ASSUNTOS_PUBLICOS_25OUT.csv contém questões observadas nas divulgações públicas, com classificação RP/PA, páginas e consequências. A avaliação PT450_QUADRO_DE_AVALIACAO_SEM_CONFUNDIR_ANOMALIAS.csv registra separadamente questões públicas, alerts simulados, conclusões ANTES da leitura do gabarito e o fato de que nenhuma distorção das contas da Auren foi comprovada. Essa segregação preserva ceticismo e evita transformar KAM da PwC em achados do aluno.')
H('8. Segunda leitura independente: um resultado verificável por PT')
items={
'EC':('A referência ao arcabouço conceitual foi revisitada frente à apresentação consolidada e individual da DFP; distinção entre normas contábeis e procedimentos de auditoria.','A estrutura conceitual não representa um teste de saldo; apenas orienta afirmações de representação fidedigna.'),
'200':('Conferidos objetivos de segurança razoável, evidência apropriada e ceticismo para as estimativas de energia e impairment.','O estudo não emite opinião e não conclui segurança razoável sobre a entidade.'),
'210':('Reconferidas precondições e documentação de aceite de trabalho; não há contrato ou carta de contratação neste estudo.','A ausência de contratação real permanece [PA] e não foi ocultada.'),
'220':('Confrontada documentação dos papéis com a necessidade de direção e revisão; campos de revisor permanecem vazios.','Sem revisão por terceiro não há alegação de validação independente.'),
'230':('Reconciliados caminhos reais para arquivos gerados, documentação do gerador e gabaritos separados.','Os códigos V2 e V3 são distintos; o histórico não foi sobreposto.'),
'240':('Reexecutados 6 mil lançamentos sintéticos por partidas dobradas e 21 sinais de risco.','Sinais simulados não são fraude confirmada; autorização e trilhas reais faltam [PA].'),
'250':('Conferida referência à regulação ANEEL/CCEE, curtailment e ressarcimentos na Nota 20.','A interpretação de obrigação depende de legislação e documentação operacional [PA].'),
'260':('Conferida a governança declarada publicamente com o conteúdo da política enviada.','Comunicações formais aos responsáveis reais não ocorreram [PA].'),
'265':('Cadastro separado de assuntos públicos criado e confrontado com PT450 antes do gabarito.','Risco público sem teste de controle interno não configura deficiência comprovada.'),
'300':('Reavaliado planejamento diante de empréstimos, combinações de negócios e ativos de energia.','A execução se restringe ao acesso público e dados didáticos.'),
'315':('Reavaliados riscos por afirmação: existência de PPE, mensuração de contratos, impairment e endividamento.','Não foram simuladas entrevistas ou walkthroughs internos como se realizados.'),
'320':('Recalculada materialidade didática com base nos ativos de R$48.727.388 mil em 2025.','Percentuais escolhidos são julgamento acadêmico, não percentuais prescritos pela NBC TA.'),
'330':('Correspondência entre riscos identificados e respostas planejadas foi reconferida por ciclo.','Confirmação de controles relevantes exigiria evidência interna [PA].'),
'402':('Indagação de organizações prestadoras de serviços na operação de comercialização revisada.','Relatórios tipo 1 ou 2 e contratos não inspecionados [PA].'),
'450':('Assuntos públicos e exceções do razão/cadastro sintéticos separados em dois registros.','Nenhum valor de distorção monetária da companhia foi estabelecido.'),
'500':('Conferida diferença entre evidência primária DFP, comunicado e cálculo que só prova consistência interna.','Conciliação construída V3 não corrobora existência de bens reais.'),
'501':('Nota 13(b) obras em andamento e peças sobressalentes de R$134.102 mil conferida na DFP p.97.','Inventário físico e litígios exigem acesso e respostas de terceiros [PA].'),
'505':('Confirmada inexistência de confirmações enviadas ou recebidas; modelos são apenas plano.','Ausência de confirmação não pode ser compensada com resposta inventada.'),
'510':('Comparativos 2024 da DFP 2025 extraídos e identificados por período e página.','Não substituem procedimentos reais sobre saldos iniciais nem auditor anterior.'),
'520':('298 linhas de BP/DRE/DFC dos períodos 2025 e 2024 extraídas; lucro consolidado do Relatório da Administração conciliado à DRE com mero arredondamento.','Expectativas externas independentes e efeitos de mudanças de perímetro ainda não fechados.'),
'530':('600 amostras estratificadas distinguidas de MUS; roteiro estatístico documentado.','Nenhuma extrapolação monetária de risco ou limite superior sem evidência auditada.'),
'540':('Componentes Nota 13(a), PPA, recuperabilidade e Nota 20 cotejados com valores públicos.','Fluxos descontados e modelos internos permanecem [PA].'),
'550':('Comunicado de 26/02/2026 e política de agosto de 2026 analisados com datas corretas.','Política de agosto não foi utilizada como regra vigente em fevereiro.'),
'560':('Fatos em 2025, até relatório PwC de 03/03/2026 e posteriores segregados.','Anúncio da reorganização em abril não altera retroativamente o grupo em dezembro.'),
'570':('Conferidos passivos e gráfico da Nota 15(b): soma R$24.521.253 mil incluindo juros futuros.','O total de fluxo futuro não foi classificado como dívida contábil reconhecida.'),
'580':('Reconhecida ausência de carta de representações real assinada.','Minutas e modelos não foram classificados RP.'),
'600':('Fato de 14/04 e conclusão da incorporação em 31/05/2026 comparados.','Componentes, materialidade e coordenação de auditores sem acesso permanecem PA.')}
assert len(items)==27
for code,(test,lim) in items.items():
 H(f'PT {code} — §6.7 Segunda leitura crítica')
 P('Conferência efetiva: '+test)
 P('Limite e conclusão fundamentada: '+lim)
 P('Revisão metodológica: evidência [RP] apenas quando documentalmente pública; resultados da nova base e dos lançamentos são [SD]; procedimentos sem acesso interno permanecem [PA]. Esta conferência é uma autorrevisão acadêmica e não uma revisão independente de outro auditor.')
 # Append individual second reading sections; avoid duplicating if script re-run
 path=R/'PT'/f'PT_{code}.md'
 if path.exists():
  text=path.read_text(encoding='utf-8')
  marker='## §6.7 — Segunda leitura crítica (25/10/2026)'
  text=text.split(marker)[0].rstrip()+f'\n\n{marker}\n\n**Conferência realizada:** {test}\n\n**Limitação e conclusão:** {lim}\n\n**Natureza:** RP exclusivamente para documentos públicos lidos, SD para simulações, PA para evidências internas não obtidas. A conferência é autorrevisão, não revisão independente.\n'
  path.write_text(text,encoding='utf-8')
H('9. Mapa de limitações e publicabilidade')
P('Não executado nesta revisão: conciliação independente PDF × CSV estruturados de dados abertos CVM (tentativa de acesso falhou); inspeção da íntegra da política original de 2022, contratos de energia, laudos de impairment, razão e documentos reais; testes de controles de empresas do grupo; verificação exaustiva da pertinência normativa de cada item; publicação no GitHub e revisão por pessoa independente. Nenhuma dessas pendências foi classificada como concluída. Para a entrega acadêmica, a existência dos procedimentos PA com planos detalhados é parte legítima do escopo do professor.')
P('Fontes e saídas de referência: fontes/AUREN_DFP_2025.pdf, físico p.96, 97, 106, 112-113, 116-117, 148-152; analises/DFP_2025_2024_EXTRAIDA_PDF_BP_DRE_DFC.csv; planilhas/DFP_REAL_E_CONCILIACOES_V3.xlsx; dados_sinteticos_v3/; documentacao/PT265_CADASTRO_ASSUNTOS_PUBLICOS_25OUT.csv; documentacao/PT450_QUADRO_DE_AVALIACAO_SEM_CONFUNDIR_ANOMALIAS.csv; resultados/QA_CHECKLIST_25OUT.json.')

def draw(c,doc):
 c.saveState();c.setFont('Helvetica',7);c.drawString(2*cm,1.5*cm,'AUREN | ADENDO DIDÁTICO | RP/PA/SD');c.drawRightString(19*cm,1.5*cm,f'{doc.page}');c.restoreState()
SimpleDocTemplate(str(annex),pagesize=(21*cm,29.7*cm),rightMargin=2*cm,leftMargin=2*cm,topMargin=2*cm,bottomMargin=2.2*cm).build(story,onFirstPage=draw,onLaterPages=draw)
with fitz.open(str(base)) as first,fitz.open(str(annex)) as addon:
 doc=fitz.open();doc.insert_pdf(first);doc.insert_pdf(addon)
 doc.set_metadata({'title':'Dossie de Auditoria Auren 2025 - revisao checklist','author':'Acadêmico - matrícula 232037730','subject':'Analise academica com RP PA SD; sem opiniao independente'})
 doc.save(str(final),garbage=4,deflate=True)
 print(json.dumps({'original_paginas':len(first),'adendo_paginas':len(addon),'final_paginas':len(doc),'pdf':str(final)},ensure_ascii=False))
