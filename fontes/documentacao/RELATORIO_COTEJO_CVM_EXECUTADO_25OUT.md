# Conciliação executada — DFP Auren 2025: PDF × dados abertos CVM

**Data:** 25/10/2026 · **Natureza:** RP (extração pública efetivamente executada) · **Escopo:** CNPJ 28.594.234/0001-23, data de referência 31/12/2025, DFP versão 1.

## Arquivo primário

Fonte: https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2025.zip  
Arquivo integral: `fontes/cvm/dfp_cia_aberta_2025.zip`  
SHA-256: `cdce6cc0e0bb85128d48928a697841f66019965bf120858c6d9802a8b70f1184`.  
O ZIP contém dados de várias companhias. Foram selecionados **somente os registros da Auren**, sem assumir que o ZIP é exclusivo da companhia.

## Método e execução

O script `codigo/44_baixar_cvm_e_conciliar.py` lê os CSVs originais diretamente do ZIP; seleciona CNPJ, data de referência, última versão, tipo de demonstração, escopo, código da conta e as colunas ÚLTIMO (2025) e PENÚLTIMO (2024); normaliza os valores à escala R$ mil; cruza com 298 contas previamente transcritas do PDF consolidado e individual em `analises/DFP_2025_2024_EXTRAIDA_PDF_BP_DRE_DFC.csv`.

- Linhas CVM extraídas da Auren, nos dois exercícios: **1226** (inclui linhas não cobertas pelas 298 contas do cotejo).
- Contas presentes na extração anterior do PDF: **298**.
- Comparações anuais realizadas: **596**.
- **Conciliadas:** **596**.
- Divergentes: **0**; sem correspondência: **0**; múltiplos valores: **0**.

## Evidência e conclusão

Todas as **596 comparações de valores de BP, DRE e DFC**, para 2025 e 2024, entre as demonstrações **consolidadas e individuais** consideradas, coincidiram com os registros disponíveis nos CSV oficiais. A conciliação documentada é o resultado de teste aritmético e de correspondência por conta, não um exame integral de todas as rubricas ou notas explicativas e não constitui opinião de auditoria sobre a Auren.

Evidências produzidas: `analises/CVM_AUREN_2025_2024_EXTRAIDA.csv`, `analises/COTEJO_PDF_VS_CVM_2025_2024.csv` e `analises/RESULTADO_COTEJO_CVM.json`. Comparações filtráveis por ano, conta, escopo e demonstração.

**Limite:** A extração PDF abrange 298 linhas de BP, DRE e DFC. A análise não inclui a totalidade dos quadros da DFP, notas, atos societários, conferências externas ou lançamentos internos. Também não autentica, isoladamente, o conteúdo original registrado pela companhia ou sua conformidade material.

## Referência cruzada com PT

- PT 500: natureza, consistência e confiabilidade da evidência documental;
- PT 510: dados comparativos e saldos iniciais, como confronto público e não substituição de trabalho sobre abertura;
- PT 520: comparação quantitativa 2025/2024 e desdobramento de variações;
- PT 230: arquivo de trilha, parâmetros e hash de fonte.

**Segunda leitura:** verificado que CONTROLADORA no PDF corresponde a INDIVIDUAL no CSV e DFC corresponde ao CSV DFC_MI (método indireto). Essa normalização corrigiu falsos registros 'sem correspondência' no processamento inicial. A versão do script entregue já contém essa correção.
