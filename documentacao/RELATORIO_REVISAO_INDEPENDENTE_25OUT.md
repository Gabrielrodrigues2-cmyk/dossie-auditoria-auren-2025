# Relatório de revisão documental independente — 25/10/2026

**Referências históricas que apontavam a anexos ausentes:** 18. Foram marcadas como NÃO ENTREGUE, não foram substituídas por dados inventados.

## 1. Escopo de revisão

Foram confrontados os papéis de trabalho em Markdown, o conjunto de fontes públicas, a conciliação CVM registrada, duas bases sintéticas, a matriz de normas, os programas, os scripts e a estrutura de publicação. A inspeção automática não substitui julgamento independente sobre suficiência das evidências.

## 2. Achado QD-01: referências documentais ausentes

Foram identificados 18 caminhos de anexos/analises citados historicamente, mas não incluídos no pacote. A lista completa e os PT afetados constam em documentacao/CONTROLE_REFERENCIAS_INDISPONIVEIS_25OUT.csv. As referências foram sinalizadas nos PT; não são válidas como provas de teste executado. Não foram inventados resultados para preencher essas lacunas.

## 3. Achado QD-02: comando de reprodução versus verificação

O script 41 regenera resultados de versões históricas e pode produzir outros PDFs; portanto, não é correto apresentá-lo como reprodutor integral do PDF definitivo. Foi disponibilizado o script 46 de leitura apenas, para pré-entrega, sem alterar documentos. O PDF final permanece artefato controlado. A reexecução completa de cada rotina modificadora deve ser documentada separadamente.

## 4. Dados sintéticos e PT 530

A V3 constitui o cadastro principal de 500.000 ativos fictícios calibrado à Nota 13(a). A V2 é a população utilizada na amostra de 600 e no detector de 982 sinalizações. A existência de ambas não autoriza combinar os resultados nem qualificá-los como MUS. Sem distorções monetárias individualmente verificadas não há projeção substantiva válida.

## 5. Conferência com a CVM

O resultado publicado contém 596 correspondências para 298 contas e dois exercícios, dentro do escopo especificado. A conciliação confirma apenas as rubricas comparadas ao mesmo conjunto de dados, não a autenticidade dos lançamentos subjacentes, nem todos os anexos, divulgações ou eventos de 2026.

## 6. Referências normativas e fundamentação

A matriz operacional contém dispositivos vinculados a procedimentos; a precisão da aplicabilidade temporal e a análise interpretativa de cada norma não se confundem com localização literal. Para o PT 530 o texto consolidado do professor apresenta requisitos de desenho, tamanho, seleção, avaliação e projeção; o exercício SD não demonstra cumprimento pleno dos requisitos aplicáveis a um trabalho real.

## 7. Limitações residuais essenciais

Continuam PA os procedimentos dependentes de balancetes, contratos, documentação contábil, controles internos, confirmações, atas, auditores de componentes e suporte de impairment. A revisão humana e a URL pública efetiva de GitHub não foram executadas. A ausência de acesso deve ser explicitamente reconhecida, jamais suprida com evidência fictícia.

## 8. Conclusão de controle de qualidade

A estrutura está apta a uma revisão acadêmica da organização dos materiais, desde que as referências históricas sinalizadas não sejam tratadas como documentos presentes. A conclusão não atribui nota, não valida julgamentos de asseguração e não equivale a emissão de opinião profissional.

**Verificação:** `python codigo/46_preflight_independente.py`. Resultado de pré-entrega não é parecer de auditoria independente.
