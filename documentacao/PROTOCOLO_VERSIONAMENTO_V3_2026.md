# Protocolo de versionamento e consistência — C6 (12/11/2026)

## 1. Versão prevalecente e critérios de leitura

**Uma única população principal:** `dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz` (V3). A composição sintética é calibrada aos quatro componentes da Nota 13(a) e aos saldos informados, sem pretensão de representar a escrituração original. Arquivos da V2 e códigos 26–29 somente permitem reproduzir a evolução histórica do exercício. Os dados V2 **não são evidência adicional** da população V3.

## 2. Cadeia única da análise V3

| Etapa | Referência que governa o resultado | Natureza |
|---|---|---|
| População | `dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz` | SD |
| Dicionário | `documentacao/DICIONARIO_V3.md` | SD |
| Conciliação | `dados_sinteticos_v3/CONCILIACAO_V3.json` | SD; totais calibrados à DFP |
| Gerador | `codigo/35_reconstruir_analitico_v3.py` | SD |
| Seleção estatística | `codigo/47_pt530_amostragem_v3_estatistica.py` | SD |
| Amostra | `analises/PT530_V3_AMOSTRA_E_TESTES_600.csv` | SD |
| Intervalos e decisão | `analises/PT530_V3_INTERVALOS_E_DECISAO.csv` | SD |
| Amostra dirigida (separada) | `analises/PT530_V3_ITENS_CERTEZA_40.csv` | SD |
| Síntese e premissas | `analises/PT530_V3_PLANO_E_RESULTADOS.json` | SD |
| Desenho escopo de grupo | `codigo/48_pt600_escopo_materialidade_segmentos.py` | SD/PA |
| Relatório de auditoria de versão | `documentacao/RESULTADO_VALIDACAO_VERSOES_V3.json` | QA documental |

## 3. Resultados que pertencem exclusivamente à V3

- N=500.000 bens artificiais únicos; população operacional N=497.280; direito de uso N=2.720.
- Sorteio separado: n operacional=450, 0 desvios observáveis, limite superior unilateral de 95%=0,6635%; n direito de uso=150, 1 desvio, limite=3,1234%; tolerância didática 2%.
- 40 itens de alto valor examinados por certeza **fora** da inferência aleatória.
- Os limites são taxas de desvio de atributos artificiais, não probabilidade de erro contábil real ou MUS.

## 4. Arquivos históricos V2 — NÃO SOMAR AO RESULTADO V3

A base V2 é mantida apenas como trilha histórica: 500 mil bens sintéticos, amostra antiga 597+3, detector global sinalizou 982 IDs, 783 coincidiram com plantios, 199 foram alertas sem plantio e 501 plantios não foram sinalizados. A V2 tinha outro desenho/calibração, de modo que os números **não** podem ser transportados à V3. Todos os arquivos com nome `PT530_V2_*`, geradores `26_*` a `29_*` ou o dicionário V2 devem ser lidos somente nesta categoria.

## 5. Hierarquia documental e limitações

Vigentes: README (este protocolo), PT 530 metodologia principal V3, PT 600 escopo por agrupamento público, análises V3 e scripts correntes. O PDF contém um adendo no início com esta hierarquia; o restante preserva o histórico de desenvolvimento, devendo eventuais trechos pré-correção ser entendidos como acervo histórico. A ausência de acesso a documentos internos continua [PA]. Revisão independente assinada não ocorreu.

## 6. Teste obrigatório antes de atualizar o GitHub

`python codigo/50_validar_versionamento_v3.py`

O comando somente lê dados e documentos, confirma N, colunas, amostra, limites, 27 PT e a inexistência de rótulo V2 como base oficial no início dos PT. Não altera bases ou resultados.
