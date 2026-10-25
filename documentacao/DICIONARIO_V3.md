# Dicionário de dados — base principal V3 (500.000 ativos fictícios)

**Fonte:** `dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz`. Cabeçalho conferido diretamente no arquivo em 25/10/2026. A base não contém marcadores `alertas`, `erro` ou os rótulos do gabarito. O arquivo GABARITO_V3_RESTRITO.csv é exclusivamente um controle didático pós-teste, nunca evidência da companhia.

| Coluna efetiva (ordem do CSV) | Tipo / unidade | Significado e limitação |
|---|---|---|
| `id_ativo` | Texto | Identificador fictício único por ativo; não representa cadastro real. |
| `escopo_dfp_2025` | Categoria | Segmentação didática IMOBILIZADO_OPERACAO ou DIREITO_USO; base para conciliar totais públicos. |
| `classe_sintetica` | Categoria | Classe operacional inventada para diversificar perfis e riscos; não é classe observada na Auren. |
| `porte_modelado` | Categoria | Estrato modelado de porte (âncora de alto valor ou pulverizado); premissa de distribuição fictícia. |
| `custo_bruto_rs` | Inteiro; R$ | Custo bruto positivo modelado e calibrado globalmente à Nota 13(a), sem suporte individual real. |
| `depreciacao_acumulada_rs` | Inteiro; R$ | Montante acumulado de depreciação simulado, deduzido no cálculo do saldo. |
| `mais_valia_ppa_rs` | Inteiro; R$ | Mais-valia de PPA simulada e calibrada globalmente ao quadro da Nota 13(a). |
| `amortizacao_ppa_rs` | Inteiro; R$ | Amortização da mais-valia simulada, deduzida no cálculo do saldo. |
| `valor_liquido_rs` | Inteiro; R$ | Saldo por ativo: custo_bruto_rs − depreciacao_acumulada_rs + mais_valia_ppa_rs − amortizacao_ppa_rs. |
| `ano_inicio_operacao` | Inteiro; ano | Ano hipotético de início de operação, utilizado para testar coerência temporal. |
| `vida_util_modelada_anos` | Inteiro; anos | Vida útil didática, não equivalente a laudo de engenharia nem a política real por ativo. |
| `documento_sintetico` | Texto | Código de suporte inteiramente fabricado; não é nota fiscal nem registro oficial. |

## Regras de conciliação e escopo

- **Identidade por linha:** `valor_liquido_rs = custo_bruto_rs - depreciacao_acumulada_rs + mais_valia_ppa_rs - amortizacao_ppa_rs`. Verifique usando o código `codigo/35_reconstruir_analitico_v3.py` e o arquivo `dados_sinteticos_v3/CONCILIACAO_V3.json`.
- **População:** 500.000 identificadores exclusivos, modelagem inteiramente fictícia com semente determinística; totais calibrados aos componentes da Nota 13(a) da DFP 2025. Essa igualdade não constitui evidência de existência, integridade ou avaliação de bens reais.
- **Escopo:** a Nota 13(a) trata do imobilizado operacional; o total de imobilizado do balanço também inclui direito de uso. A conciliação separa os dois escopos, evitando compará-los indevidamente.
- **Seleção amostral:** as análises de 600 registros mantidas no PT 530 utilizam a **V2**, não esta V3. Não afirmar que seus alertas são resultados sobre a V3.
- **Controle do gabarito:** o gabarito de erros só pode ser consultado após o detector cego; não deve estar agregado ao CSV da população.
