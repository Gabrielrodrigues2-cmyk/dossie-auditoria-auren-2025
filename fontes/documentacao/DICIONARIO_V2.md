# Dicionário DEFINITIVO — população V2 publicada

**12 campos efetivos.** Não há `alertas`, `indicador_suporte`, `unidade_operacional_sintetica` ou outros campos de rótulos no CSV público. Os dados são 100% artificiais.

| Campo | Interpretação |
|---|---|
| `id_ativo` | Identificador exclusivamente fictício e único do bem |
| `escopo_dfp_2025` | Subgrupo do BP usado na calibração: operação ou direito de uso |
| `classe` | Classe didática (igual ao escopo, sem classes operacionais reais) |
| `data_aquisicao_original` | Data hipotética; datas posteriores ao fechamento são anomalias sem rótulo |
| `data_inicio_depreciacao_hipotetica` | Início da depreciação hipotética; no gerador coincide com a data de aquisição |
| `vida_util_anos_original` | Vida útil original do cenário simulado em anos |
| `vida_util_anos_modelada` | Vida útil modelada em anos; 99 pode sinalizar exceção |
| `custo_bruto_hipotetico_rs` | Custo bruto artificial em reais inteiros, não concilia com custo bruto real |
| `depreciacao_acumulada_hipotetica_rs` | Depreciação acumulada artificial em reais inteiros; não é valor real |
| `valor_liquido_rs` | Valor líquido fictício em R$; totais calibrados aos dois subgrupos do BP |
| `despesa_depreciacao_2025_hipotetica_rs` | Despesa anual aproximada fictícia em R$; sem reprodução da depreciação 2025 divulgada |
| `documento_sintetico` | ID artificial do documento; duplicidade intencional pode aparecer |

**Gabarito:** `dados_sinteticos_v2/gabarito_v2_SEPARADO.csv`; contém `id_ativo,anomalia_plantada`, armazenado separadamente da população e consultado apenas depois da detecção. O gabarito não deve ser distribuído como se fosse evidência real.
