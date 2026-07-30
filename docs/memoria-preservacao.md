# Memória e preservação do acervo

## Compromisso

A sanitização do repositório não elimina a memória do Coletivo Terra Viva. Ela separa:

- **memória pública:** fatos validados e autorizados para divulgação;
- **acervo de trabalho:** conversas, propostas, registros e versões usadas na curadoria;
- **documentação sensível:** dados pessoais, bancários, administrativos, territoriais e
  autorizações;
- **evidência candidata:** material que pode sustentar uma afirmação depois de validado.

Remover um arquivo do índice Git não significa apagá-lo do acervo local. A publicação
deve conter sínteses rastreáveis, e não cópias indiscriminadas dos documentos de origem.

## Conjuntos históricos preservados localmente

| Conjunto | Conteúdo | Situação |
|---|---|---|
| Conversa direta com Murilo | articulações de maio, convites, documentos e tecnologias | arquivo interno |
| Grupo Juventude Solidária | elaboração, inscrição, recurso, continuidade e prospecções | arquivo interno |
| Propostas do viveiro | versões simples, versões com bambu e gabaritos | arquivo de trabalho |
| Documentos do projeto | orçamento, formulários e anexos | acesso restrito |
| Projeto ECOSALA Itinerante | concepção de apoio territorial e agroecológico | referência interna |
| Imagens, mapas e mídias | registros visuais e cartográficos | publicação condicionada a autorização |
| Documentos administrativos | atas, estatuto, dirigentes e cadastros | acesso restrito |

Os conjuntos permanecem nas pastas locais historicamente utilizadas, inclusive
`TRIAGEM-BRUTA`, `02_PROPOSTAS`, `07_DOCUMENTOS_PROJETO` e `13_PROJETOS`. Essas pastas
não devem ser adicionadas ao Git público.

Em 30 de julho de 2026, os 402 arquivos existentes na `TRIAGEM-BRUTA` da cópia histórica
`MST-Mario_Lago` foram copiados integralmente para a `TRIAGEM-BRUTA` deste repositório
canônico. A comparação entre origem e destino não apresentou diferenças. A cópia de
origem foi mantida, oferecendo redundância durante a transição.

## Cadeia de validação

Cada informação usada externamente deverá possuir:

1. afirmação objetiva;
2. fonte ou registro de origem;
3. data ou período;
4. pessoa responsável pela validação;
5. classificação de acesso;
6. autorização de publicação, quando necessária;
7. versão e data da última revisão.

## Preservação mínima recomendada

- manter uma cópia principal e uma cópia de segurança em ambiente privado;
- conservar os arquivos originais, sem alterar metadados ou nomes;
- produzir inventário com nome, tamanho, data e hash dos arquivos;
- registrar novas versões sem substituir os originais;
- restringir acesso por pasta e finalidade;
- revisar periodicamente links compartilhados;
- recolher autorizações separadas para imagem, voz e depoimento;
- não usar GitHub público ou página MkDocs como arquivo administrativo.

## Lacuna de segurança

A versão pública atual poderá ser sanitizada, mas commits antigos do Git ainda podem
conter documentos que foram publicados anteriormente. A eliminação dessa exposição
histórica exige uma operação própria de reescrita do histórico e nova publicação, com
autorização expressa e cópia de segurança prévia.
