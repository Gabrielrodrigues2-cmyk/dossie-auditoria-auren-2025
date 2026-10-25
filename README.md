# Auren Energia S.A. — Dossiê acadêmico de auditoria do exercício de 2025

**Universidade de Brasília (UnB) · CCA0024 — Auditoria 1 · Matrícula 232037730 · Data de preparação: 25/10/2026.**

**Natureza:** exercício acadêmico baseado em demonstrações públicas e dados fictícios; não é auditoria independente da Auren e não emite opinião de asseguração.

## Comece por aqui

1. **Dossiê oficial em PDF (único):** [`dossie/DOSSIE_AUREN_2025_REVISAO_NORMATIVA_OPERACIONAL.pdf`](dossie/DOSSIE_AUREN_2025_REVISAO_NORMATIVA_OPERACIONAL.pdf). Contém 27 PT e referências cruzadas. Arquivos de versões antigas foram excluídos da pasta `dossie/` para evitar erro de escolha.
2. **Papéis individuais:** `PT/PT_EC.md`, `PT/PT_200.md` a `PT/PT_600.md` (todos os 27 identificados na [`MATRIZ_COBERTURA_NORMAS_ATUALIZADA.csv`](documentacao/MATRIZ_COBERTURA_NORMAS_ATUALIZADA.csv)). Programas individuais em `programas/` e seis programas de ciclo em `ciclos/`.
3. **Base sintética PRINCIPAL V3:** [`IMOBILIZADO_500000_V3_CEGO.csv.gz`](dados_sinteticos_v3/IMOBILIZADO_500000_V3_CEGO.csv.gz) — 500.000 registros inventados. **Dicionário correto:** [`DICIONARIO_V3.md`](documentacao/DICIONARIO_V3.md). Conciliação sintética `dados_sinteticos_v3/CONCILIACAO_V3.json`. O arquivo público não contém rótulos de erro.
4. **Base V2 separada:** `dados_sinteticos_v2/imobilizado_500000_v2_REGERADO.csv.gz`, dicionário [`DICIONARIO_V2.md`](documentacao/DICIONARIO_V2.md); usada **especificamente** na amostra de 600 e na detecção de 982 sinalizações. Não transferir esse resultado à V3.
5. **Razão inteiramente fictício:** `dados_sinteticos_v3/RAZAO_PT240_12000_LINHAS.csv`, para aplicação didática de testes no PT 240.
6. **Cálculos e planilhas:** `planilhas/PT_320_materialidade_e_cobertura.xlsx` e `planilhas/DFP_REAL_E_CONCILIACOES_V3.xlsx`; arquivos CSV em `analises/` e `documentacao/`.
7. **Matriz de normas:** [`MATRIZ_COBERTURA_NORMAS_ATUALIZADA.csv`](documentacao/MATRIZ_COBERTURA_NORMAS_ATUALIZADA.csv), mais `MATRIZ_PERTINENCIA_NORMATIVA_OPERACIONAL_27_PT.csv` e o PDF `NORMAS/Consolidado Normas Aud1.pdf` do professor.
8. **Relação de fontes:** [`REGISTRO_FONTES_VERIFICADAS.csv`](documentacao/REGISTRO_FONTES_VERIFICADAS.csv) com documento, página, URL conhecida, nível de verificação e hash; URLs genéricas estão expressamente marcadas como **não sendo URLs diretas dos PDFs**.
9. **Cotejo independente com a CVM:** `fontes/cvm/dfp_cia_aberta_2025.zip` e `analises/COTEJO_PDF_VS_CVM_2025_2024.csv`; na seleção de 298 rubricas × 2 exercícios foram reportadas 596 correspondências. Não generalizar para notas não testadas.

## Reproduzir e testar

```bash
python -m pip install -r requirements.txt
python codigo/46_preflight_independente.py
# Opcional: regenerar resultados (pode alterar arquivos existentes e exigir dependências):
python codigo/41_reproduzir_entrega.py
python codigo/44_baixar_cvm_e_conciliar.py
```

Os comandos pressupõem execução **na raiz do repositório** e Python compatível com `requirements.txt`. Os dados abertos CVM estão incluídos para uso offline. O pipeline gera/valida cálculos e bases; **não reconstrói integralmente, a partir de Markdown, todas as páginas do PDF**. Os geradores em `codigo/` com nomes históricos não substituem o PDF oficial.

## Classificação transparente dos procedimentos

**[RP]** Inspeção/recálculo de fonte pública realmente realizado; **[SD]** experimento com dados artificiais; **[PA]** trabalho planejado e não executado por falta de registros internos/autorizações. A base não corresponde ao razão real da companhia; os valores da Nota 13 são alvos de calibração. O PT 530 **não é MUS** e não contém projeção monetária substantiva validada. Campos de revisão permanecem sem assinatura.

## Documentação da entrega

- [`MATRIZ_REQUISITOS_ENTREGA_ATUALIZADA.csv`](documentacao/MATRIZ_REQUISITOS_ENTREGA_ATUALIZADA.csv): requisito → arquivo → verificação.
- [`RELATORIO_CONFERENCIA_ENTREGA_25OUT.md`](documentacao/RELATORIO_CONFERENCIA_ENTREGA_25OUT.md): correções aplicadas e limitações.
- `MANIFESTO_SHA256_FINAL.csv`: hashes SHA-256 do conteúdo entregue (exceto o próprio manifesto).

**Publicação obrigatória:** descompactar e publicar em repositório **público** do GitHub, testar link em janela anônima e enviar a URL no Aprender UnB. A publicação e eventual revisão humana **não foram executadas nem simuladas por este pacote**.


## Revisão independente final de integridade (25/10/2026)

Execute **`python codigo/46_preflight_independente.py`** antes de publicar. O comando apenas lê os arquivos e confere bases, conciliação CVM, planilhas essenciais, SHA das fontes, PT e sintaxe dos códigos, sem modificar resultados. A revisão identificou referências históricas sem arquivo correspondente; elas foram sinalizadas explicitamente nos PT e listadas em `documentacao/CONTROLE_REFERENCIAS_INDISPONIVEIS_25OUT.csv`. Não trate como concluídos os testes vinculados a tais anexos. O PDF inclui um parecer de pré-entrega com os mesmos limites. O gerador de resultados é distinto deste verificador e não reproduz de forma integral o dossiê PDF.

## Revisão final de suficiência das evidências

**Leia antes de interpretar os resultados:** `documentacao/RELATORIO_SUFICIENCIA_FINAL_25OUT.md` e `documentacao/MATRIZ_SUFICIENCIA_E_LIMITACOES_27_PT.csv`. Os 27 papéis e o PDF contêm uma seção §7 individual de evidência, limitação e efeitos. Dados fictícios não são prova sobre a Auren; revisão independente não foi efetuada.
