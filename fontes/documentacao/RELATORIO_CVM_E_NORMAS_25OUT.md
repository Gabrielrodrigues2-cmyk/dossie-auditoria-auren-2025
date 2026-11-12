# Conferência adicional — DFP CVM e itens NBC TA (25/10/2026)

## 1. Dados abertos CVM: situação documentada

**URL oficial verificada:** https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2025.zip

O catálogo oficial da CVM disponibiliza o arquivo anual e informa atualizações periódicas. **Neste ambiente o ZIP não foi baixado**, devido a falha de acesso binário/rede. Não declarar o cotejo como concluído; o `COTEJO_PDF_VS_CVM_2025.csv` só será gerado após execução bem-sucedida.

**Procedimento de fechamento:** colocar o ZIP original obtido da CVM em `fontes/cvm/dfp_cia_aberta_2025.zip`, ou executar o comando abaixo em ambiente com internet:

```bash
python codigo/44_baixar_cvm_e_conciliar.py
```

O script seleciona o CNPJ 28.594.234/0001-23, data-base 31/12/2025, última apresentação de versão disponível, compara contas entre os 298 registros extraídos do PDF e as tabelas da CVM por escopo, demonstração e código, e escreve divergências com valores e página da DFP. Revisar eventuais distorções da classificação de códigos e unidades (R$ mil); não tomar igualdade como prova de completude de auditoria.

## 2. Normas do professor: natureza da verificação

Fonte efetivamente inspecionada: `Consolidado Normas Aud1.pdf` (1479 páginas, fornecido anteriormente).

- `documentacao/AUDITORIA_NORMAS_27_PT_2025.csv`: matriz por PT com versão constante no consolidado, intervalo de páginas, itens mencionados e exemplos textuais.
- `documentacao/ITENS_NORMATIVOS_LOCALIZACAO.csv`: conferência de localização da numeração de cada item mencionado e página física respectiva, com pequenos excertos.
- `documentacao/RESUMO_CONF_NORMAS.json`: contagem automática.

**Escopo alcançado:** checagem de que os números de itens referidos nos PT estão presentes na seção correspondente do documento do professor. **Não equivale** a uma revisão jurídica de vigência e aplicabilidade de todas as revisões normativas no exercício de 2025, nem a uma conclusão de que toda interpretação de PT está correta. As alterações publicadas em 2026 com vigência para exercícios futuros não devem ser aplicadas retroativamente sem fundamento.

**Exemplo controlável:** na NBC TA 530, os itens 6 a 9 tratam do desenho, tamanho, seleção e execução de testes, enquanto os itens 14 e 15 exigem avaliar projeção de distorções *nos testes de detalhes* e a razoabilidade da base de conclusão. O estudo não tem distorções monetárias por item efetivamente verificadas; portanto não fabricar projeção.

## 3. Próximos passos antes da submissão

1. Executar importação do ZIP da CVM em máquina com internet e anexar os CSVs de cotejo gerados.
2. Inspecionar divergências entre apresentações/escopos, versões, códigos e escalas.
3. Não preencher revisão/assinatura de auditor externo: trabalho didático.
