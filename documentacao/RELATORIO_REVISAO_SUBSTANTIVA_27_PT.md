# Revisão de profundidade dos 27 PT — 24/10/2026

Foi acrescentada uma seção original e específica a **cada um dos 27 PT**. A matriz QA em CSV avalia cobertura lexical mínima, **não suficiência probatória**. Conclusões são classificadas [RP], [PA] e [SD].

## Fragilidades que não podem ser resolvidas por redação

- PT 530: a amostra de 600 não foi dimensionada para projeção monetária; o teste cadastral não fornece distorções monetárias verificadas.
- PT 540: sem modelos internos e premissas auditáveis, o impairment não pode ser reexecutado integralmente.
- PT 600: não há demonstrativos e instruções de todos os componentes para concluir sobre consolidação.
- NBC TA: números e pertinência contextual dos itens precisam ser confrontados com norma oficial vigente; localização textual isolada não equivale a validação normativa.
- Fontes: URLs genéricas de páginas de RI não equivalem a URLs diretas de cada PDF.

## Controles automatizados

O script `codigo/33_qa_profundidade_27_pt.py` valida os campos mínimos, a não divulgação de coluna de alertas e a contagem de PT. O resultado não substitui parecer do professor.
