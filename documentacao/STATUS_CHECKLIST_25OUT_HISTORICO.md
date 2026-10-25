# Controle de cumprimento do checklist — 25/10/2026

Este documento diferencia **entrega existente**, **entrega parcial** e **atividade não comprovada**. A revisão foi feita com os documentos públicos enviados e a DFP 2025. Procedimentos RP, PA e SD seguem distinguidos.

| Exigência | Situação nesta edição | Evidência | Limite |
|---|---|---|---|
| Aproximação ao modelo ISA e aprofundamento dos 27 PT | Realizada — adendo crítico de cada PT | `PT/PT_*.md`, **[REFERÊNCIA HISTÓRICA NÃO ENTREGUE: dossie/DOSSIE_AUREN_2025_REVISAO_CHECKLIST.pdf]** | 138 páginas não são garantia de suficiência substantiva |
| §6.7 segunda leitura em cada PT | Realizada | Arquivos `PT/` e adendo | Autorrevisão, não revisão independente |
| Comparar lucro do relatório da administração com DRE | **Realizada** | Administração PDF físico p59: -R$557,9 mi (2025), +R$271,9 mi (2024); DRE p19: -R$557,875 mi e +R$271,869 mi | Consistente após arredondamento gerencial a 1 decimal; escopo consolidado igual |
| Perfil de vencimento dívida (P08) | Realizada | Nota 15(b), PDF físico p.106, gráfico transcrito; soma R$24.521.253 mil | Inclui juros futuros, não igualar ao passivo |
| Contratos futuros de energia Nota 18 | Leitura pública e plano detalhado | DFP física pp.112-113, PT540/500 | Modelos e contratos não disponíveis [PA] |
| Ressarcimento Nota 20 | Realizada análise pública | DFP física pp.116-117; R$900.907 mil circulante e R$688.480 mil não circulante | Testes de integridade internos [PA] |
| Planilha completa BP, DRE, DFC | **298 linhas extraídas** | `analises/DFP_2025_2024_EXTRAIDA_PDF_BP_DRE_DFC.csv`, `planilhas/DFP_REAL_E_CONCILIACOES_V3.xlsx` | Apenas linhas de BP/DRE/DFC (não 1.076 valores do modelo); extração textual precisa de revisão visual integral |
| PT 265 e 450 separados do gabarito | Realizada | `documentacao/PT265_*` e `documentacao/PT450_*` | Nenhuma distorção real confirmada |
| Bruto/depreciação/PPA Nota 13(a) | Realizada V3 adicional | `dados_sinteticos_v3/CONCILIACAO_V3.json` | Conciliação forçada por modelagem; não é evidência de saldos individuais reais |
| Ativos heterogêneos, unidades de alto valor | Realizada V3 | 40 âncoras concentram 62% do custo modelado | Pesos ficcionais, não usinas efetivamente cadastradas |
| Razão sintético do PT 240 | Realizada | 12.000 linhas, 6.000 partidas dobradas, débitos=créditos | Flags não significam fraude comprovada |
| Testes automatizados e reprodução | Realizada | `codigo/41_reproduzir_entrega.py`, `resultados/QA_CHECKLIST_25OUT.json` | Reproduz dados e PDF a partir do PDF acadêmico original incluído |
| Workbook com fórmulas | Realizada | `planilhas/DFP_REAL_E_CONCILIACOES_V3.xlsx` | Fórmulas requerem recálculo no aplicativo para exibir caches em leitores limitados |
| PDF × dados abertos CVM (P02) | **Não executada** | URL oficial identificada; tentativa de download falhou | Requer CSV da CVM ou acesso operacional à fonte |
| Consolidado das normas e conferência exaustiva (P03) | **Versões documentadas; itens pendentes** | `documentacao/INDICE_NORMAS_CONSOLIDADO_PROFESSOR.csv`, 26 normas + EC extraídas do sumário do PDF do professor | Confere etiquetas das versões do consolidado recebido, não validade semântica ou vigência jurídica de cada item |
| FRE/DFP 2024/ITRs | Parcial | FRE/DFP 2024 recebidos na conversa; comparação 2024 também constou da DFP 2025 | ITRs e cotejo documental mais amplo não concluídos |
| GitHub público | Não realizado | README com procedimentos | Depende da publicação pelo estudante |
| Revisão externa/assinatura | Não realizada | Campos em branco | Não inventar revisão |
| Acesso a contratos, documentos internos e confirmação | PA | Programas específicos | Acesso externo proibido/indisponível |

**Aviso:** O checklist enviado menciona MUS e projeção monetária como se existentes; a implementação observável do pacote atual não contém tal execução. Não foi lançada projeção sem valores verdadeiros auditáveis. A explicação estatística está em `documentacao/NOTA_METODOLOGICA_AMOSTRAGEM_25OUT.md`.
