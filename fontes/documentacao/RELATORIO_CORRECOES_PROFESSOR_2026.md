# Resposta técnica à avaliação do professor — revisão de 11/11/2026

**Nota recebida: 7,65/10 (C1 0,90; C2 1,90; C3 1,15; C4 1,40; C5 1,10; C6 0,75; C7 0,45).** Não se reivindica nota 10 automática: os pontos foram tratados com evidências e limitações verificáveis.

## C2 — NBC TA 600 e materialidade de escopo
Foi implementado `codigo/48_pt600_escopo_materialidade_segmentos.py`, com receita segmentada da Nota 4 (DFP p. física 78), conciliação da receita consolidada e quatro limiares didáticos para Geração, Comercialização, Holding/Pipeline e Ajustes/Eliminações. O PT 600 §8 contém riscos, testes previstos, documentação necessária, materialidade global e limiares específicos. **Não afirmar que são materialidades de pessoas jurídicas ou componentes reais**; isso exige balancetes e julgamento do auditor do grupo. A divergência de subtotal operacional extraído foi conservada como ressalva, não como distorção.

## C5 — NBC TA 530 e risco amostral
Novo experimento executado **sobre V3**, distinto da V2: n=450 no imobilizado operacional (k=0; CP unilateral 95%=0,6635%); n=150 no direito de uso (k=1; CP unilateral 95%=3,1234%); tolerância de atributos didática de 2%. O segundo estrato **não atende ao critério de aceitação** e exige investigação. Quarenta ativos de alto valor são analisados por certeza em arquivo próprio, sem inferência. O teste consulta o gabarito apenas após a seleção e a classificação dos atributos. A análise não é MUS, não possui distorção monetária validada e não permite projetar R$ de erros. Os 982 alertas e 501 anomalias não detectadas são do detector histórico V2, não do experimento V3.

## C6 — documentação e versionamento
README, todos os 27 PT e adendo PDF declaram expressamente V3 como população principal. A V2 é mantida por transparência histórica e para reprodução de testes anteriores, mas NÃO é a população principal. As referências históricas indisponíveis continuam expressamente não entregues; não se fabricou evidência. O novo script `codigo/49_validar_correcao_professor.py` valida as 27 retificações, a população V3, os cálculos de C2/C5 e a integridade de caminhos centrais.

## C1, C3, C4, C7 — revisão de mérito
C1: preservar escopo da conciliação PDF × CVM (298 rubricas × 2 exercícios), datas e fontes, sem confundir cotejo com auditoria. C3: vincular riscos aos limiares e testes planejados por agrupamento. C4: conferir V3 com 500 mil registros únicos e conciliação dos componentes modelados. C7: integrar resultados, distinção RP/PA/SD, limitações e ausência de opinião de auditoria.

## Ressalvas profissionais inafastáveis
Sem razão e documentação de suporte reais, modelos de impairment, contratos, pacotes por entidade, comunicações de auditores de componentes e representações formais, os testes permanecem [PA]. A calibração sintética, os intervalos de atributos e a conciliação de fontes públicas não suprem essas evidências. Não houve revisão profissional independente assinada.
