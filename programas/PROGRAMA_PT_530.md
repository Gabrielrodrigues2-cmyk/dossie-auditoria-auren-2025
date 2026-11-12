> **Versão sintética vigente:** V3 é a base principal; V2, quando referida, é apenas trilha histórica. Ver `documentacao/PROTOCOLO_VERSIONAMENTO_V3_2026.md`.

# Programa de trabalho — PT 530: Amostragem

**Empresa / exercício:** Auren Energia S.A. / 2025  
**Preparado por:** matrícula 232037730, 23/10/2026. **Revisão:** não realizada.

## Objetivo e procedimentos
Documentar população, unidade, desenho, tamanho 600, seleção, exceções e limites de projeção.

## Evidência e documentação prevista
CSV 600, base SD e gabarito separado

## Execução e resultado
Este programa documenta procedimentos RP, PA ou SD conforme o PT principal. **Não se afirma que procedimentos PA foram executados**. A classificação de cada teste e seu resultado específico devem ser confirmados no arquivo `PT/PT_530.md` do repositório principal.

## Limitações e conclusão
Estratificação não sustenta IC binomial simples. A conclusão do programa é de planejamento e avaliação acadêmica, não de asseguração independente.

## Referências cruzadas
- `PT/PT_530.md`
- `normas_indice/PT_530_INDICE_NORMATIVO.md`
- `dossie/DOSSIE_AUREN_2025_27_PT.pdf`


## Atualização da avaliação do professor (11/11/2026) — PREVALÊNCIA
A população principal atual é V3. Executar `codigo/47_pt530_amostragem_v3_estatistica.py` para selecionar 450 registros operacionais e 150 de direito de uso; testar 40 ativos âncora por certeza, sem incluir esses 40 na inferência estatística. Parâmetros SD: taxa tolerável 2%, confiança unilateral 95%; avaliar por estrato com Clopper-Pearson. O estrato direito de uso apresentou um desvio observável e limite superior 3,1234%, acima de 2%, exigindo investigação [PA]. Não projetar distorção monetária. V2 e 982 alertas são apenas histórico. Ver PT 530 §8 e arquivos `analises/PT530_V3_*`.
