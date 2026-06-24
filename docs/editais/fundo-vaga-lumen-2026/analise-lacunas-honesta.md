# 🔬 Análise de Lacunas — Base de Evidências das Tecnologias

> **Propósito:** Mapear honestamente o que existe, o que foi testado,  
> o que é hipótese, e o que precisa ser desenvolvido.  
> Nenhuma informação falsa ou inflada será incluída na proposta.

---

## 1. Status Real de Cada Tecnologia

| Tecnologia | TRL real | O que existe | O que NÃO existe | Base documental |
|---|---|---|---|---|
| **Forno MPTDF** (vapor + sal + pirolenhoso) | **TRL 4-5** | Protótipo funcional no IFB Planaltina. Testes empíricos de tratamento. Cartilha de construção. | Ensaios normatizados (ABNT). Caracterização completa de durabilidade. | Cartilha Bambu (Obsidian), Roteiro de Testes (+CEFET) |
| **Geodésicas de bambu** | **TRL 5-6** | Múltiplas construções empíricas (Rio+20, oficinas). Projeto conceitual validado. | Ensaios estruturais. Normatização. Certificação. | Labiapa (André Blanco), registros fotográficos |
| **PU Vegetal (mamona/Imperveg)** | **TRL 4** | Formulação laboratorial. Ensaios de tração. Fichas técnicas. | Aplicação em escala real. Intemperismo acelerado. Selante náutico testado. | Mentoria_Tecnologia_Takwara, Acervo MQTF |
| **Biochar** | **TRL 3-4** | Nota técnica. Estudos de produção. Aplicação em solo. | Uso como filtro de efluentes. Integração com saneamento. | Takwara-Tech (nota técnica biochar) |
| **Pirolenhoso** na caldeira MPTDF | **TRL 4** | Incorporado ao processo do forno. Dosagem 10-30% do volume. | NÃO TESTADO como biofertilizante, biodefensivo ou preservativo isolado. **Potencial não explorado.** | Roteiro de Testes, Cartilha Bambu |
| **Fossa séptica ecológica / saneamento descentralizado** | **TRL 2-3** | Conceitos da literatura. Projeto T01 (Plataforma Amazônia Regenerativa). | Protótipo construído. Teste de campo. Validação em ambiente real. | Plataforma Amazônia Regenerativa (conceitual) |
| **Embarcação catamarã de bambu** | **TRL 2-3** | Projeto conceitual com DOI/Zenodo. | Casco construído. Teste de flutuação. Integração MPTDF+PU. | Plataforma Amazônia Regenerativa (projeto) |
| **Fitossaneamento** (caldas, biofertilizantes) | **TRL 2-3** | Referências da literatura. Conhecimento do Prof. Paron (micorrizas). | Protocolo próprio. Validação em campo. | IFSP (Marcos Paron — microbiologia) |
| **Biofiltro dinâmico** | **TRL 2** | Conceito. Literatura correlata. | Protótipo. Teste hidráulico. Colonização microbiana. | Projeto conceitual |
| **Créditos de carbono** (biochar + SAFs) | **TRL 1-2** | Referências de mercado. Rota do bambu (Takwara-Tech). | Metodologia própria. Certificação. Linha de base. | Takwara-Tech (artigos conceituais) |

---

## 2. O Caso do Pirolenhoso — Quatro Potenciais Não Incorporados

O **ácido pirolenhoso** é subproduto da carbonização da biomassa (produção de biochar).  
No processo MPTDF, ele já é usado na caldeira a vapor (dosagem 10-30%).  
**Quatro aplicações potenciais estão documentadas conceitualmente mas NÃO foram testadas ou incorporadas à proposta:**

| Aplicação | Base teórica | Status | O que falta |
|---|---|---|---|
| **1. Preservativo de bambu** (pós-tratamento) | Propriedades fungicidas/bactericidas conhecidas. Já usado no vapor MPTDF. | **Hipótese** — a eficácia como preservativo isolado (sem vapor) não foi testada. | Ensaio de eficácia fungicida em corpos de prova. Comparação com CCA/CCB. |
| **2. Biofertilizante foliar/solo** | Relatos na literatura agroecológica. | **Hipótese** — sem protocolo próprio ou validação em campo. | Teste de dosagem em hortas/quintais. Análise de solo. |
| **3. Biodefensivo** (controle de pragas/doenças) | Literatura de agricultura orgânica. | **Hipótese** — sem ensaio específico para cultivos da região. | Bioensaio com pragas-alvo (hortaliças, árvores nativas). |
| **4. Redutor de emissões** (condensador MPTDF) | O forno já tem condensador que coleta o pirolenhoso. | **Instalado** — mas sem medição quantitativa de redução de emissões. | Medição de gases pré e pós-condensador. |

> **Implicação para a proposta:** Pirolenhoso pode ser citado como **aplicação atual** (no vapor MPTDF) e **potencial a ser validado** (quatro usos listados acima).  
> NÃO pode ser citado como biofertilizante ou biodefensivo validado — são hipóteses de pesquisa.

---

## 3. TRL de Partida por Subsistema (Visão Honesta)

```
Sistema Vaga Lúmen
├── 🟢 Ônibus-escola (TRL 8-9 — tecnologia madura, chassis novo)
│   ├── Painéis solares (TRL 9)
│   └── Reuso águas cinzas (TRL 2-3 — conceitual)
├── 🟡 Embarcação bambu
│   ├── Casco catamarã (TRL 2-3 — conceitual)
│   ├── MPTDF no bambu (TRL 4-5 — protótipo)
│   └── PU Vegetal selante (TRL 4 — laboratório)
├── 🟡 Saneamento ecológico
│   ├── Banheiro seco conceito (TRL 2-3)
│   ├── Biofiltro flutuante (TRL 2 — conceito)
│   └── Colonização microbiana (TRL 2 — literatura)
├── 🟢 Bioconstrução e formação
│   ├── Geodésicas bambu (TRL 5-6)
│   ├── Tintas minerais (TRL 5-6 — André Blanco)
│   └── Metodologia ECOSALA (TRL 3-4)
├── 🟡 Bioinsumos
│   ├── Biochar produção (TRL 3-4)
│   ├── Pirolenhoso 4 usos (TRL 2-3 — hipóteses)
│   └── Fitossaneamento (TRL 2-3 — literatura)
└── 🔵 Créditos de carbono (TRL 1-2 — conceitual)
```

**TRL geral de partida da proposta:** TRL 2-4 (ponderado pelo estágio mais baixo dos subsistemas inovadores).  
**TRL de chegada pretendida:** TRL 6-7 (demonstração em ambiente operacional).

> A inovação está em **integrar** subsistemas de baixa maturidade num sistema móvel funcional.  
> Isso é exatamente o que a FINEP Mais Inovação financia (TRL 3-8).

---

## 4. Lacunas Documentais nas Fichas Técnicas

| Documento | Lacuna | Ação necessária |
|---|---|---|
| **Ficha PU Vegetal** | Selante náutico não testado | Adicionar ressalva: "testes realizados apenas em ambiente laboratorial seco — sem validação em imersão ou névoa salina" |
| **Nota Técnica Biochar** | Filtro de efluentes não testado | Adicionar: "aplicação como meio filtrante é hipótese baseada em literatura — protótipo a ser construído no projeto" |
| **Roteiro de Testes MPTDF** | Ensaios normatizados ABNT não realizados | Adicionar: "parâmetros empíricos — ensaios de caracterização mecânica e durabilidade previstos como atividade de P&D do projeto" |
| **Cartilha Bambu** | Pirolenhoso como fertilizante/defensivo não validado | Adicionar: "usos descritos são potenciais identificados na literatura — validação em campo prevista" |
| **Projeto Catamarã** (DOI/Zenodo) | Apenas conceitual | Adicionar: "projeto naval preliminar — cálculo estrutural e ensaios de flutuação necessários" |

---

## 5. Proposta de Redação Corrigida para o Resumo Executivo

> *"O projeto integra doze tecnologias sociais abertas (CC-BY/Zenodo) em diferentes níveis de maturidade: o forno de tratamento térmico a vapor (MPTDF) e as estruturas geodésicas de bambu têm protótipos funcionais validados empiricamente (TRL 4-5); o selante vegetal de mamona (PU) e o biochar foram caracterizados em laboratório (TRL 3-4); os sistemas de saneamento ecológico, a embarcação catamarã e o uso do ácido pirolenhoso como biofertilizante e biodefensivo encontram-se em estágio conceitual, com referências na literatura e projetos preliminares depositados na Plataforma Amazônia Regenerativa (TRL 2-3). O desafio tecnológico do projeto consiste em integrar esses subsistemas num laboratório móvel funcional (ônibus + embarcação), elevando o conjunto ao TRL 6-7 por meio de ensaios de laboratório, prototipagem, validação em campo e demonstração operacional nos territórios de reforma agrária e APAs da região de Ribeirão Preto/SP. As referências técnicas e fichas dos materiais encontram-se nos repositórios institucionais vinculados à proposta."*

---

## 6. Resumo das Ações para Fechamento das Lacunas

| Lacuna | Ação | Prioridade | Responsável |
|---|---|---|---|
| **Pirolenhoso 4 usos** sem validação | Elaborar protocolo de ensaios (biofertilizante, defensivo, preservativo) | 🔴 Alta | Prof. Paron (microbiologia) + Fabio |
| **Biochar como filtro** hipotético | Projetar coluna de filtração para ensaios | 🔴 Alta | Equipe técnica |
| **Fichas técnicas** com ressalvas | Atualizar com notas de TRL real | 🟡 Média | Fabio (documentação) |
| **Créditos de carbono** sem linha de base | Buscar metodologia certificável (ex: VERRA) | 🟡 Média | Consultoria externa |
| **Embarcação catamarã** conceitual | Contratar engenharia naval para projeto preliminar | 🟡 Média | André Blanco + Luis Felipe |
| **Fossa séptica ecológica** sem protótipo | Construir protótipo em escala 1:1 no Mário Lago | 🟢 Baixa | Murillo + Zaqueu + André |

---

## 7. Documentos a Atualizar / Criar

| Arquivo | Conteúdo | Status |
|---|---|---|
| `docs/editais/fundo-vaga-lumen-2026/plano-revisao-vaga-lumen.md` | Este documento (análise de lacunas honesta) | ✅ Criado |
| Fichas técnicas PU Vegetal + biochar + MPTDF | Adicionar campo "TRL real" + "Limitações" | 📝 Pendente |
| Protocolo de ensaios de pirolenhoso | 4 usos: preservativo, biofertilizante, biodefensivo, redução emissões | 📝 Pendente |
| Projeto catamarã (Zenodo) | Atualizar DOI com nota "projeto conceitual — necessita validação" | 📝 Pendente |
