# AGENTS.md — Plataforma Juventude Solidária (MST Mário Lago)

## Identidade

Repositório de documentação e acompanhamento do **Viveiro-Educador de Mudas Terra Viva**, submetido ao edital **Juventude Solidária 01/2026** (Governo Federal/MEC/IFMT).

**Público-alvo:** Membros do MST e comunidade do Assentamento Mário Lago — documentação simplificada e acessível.

**Resultado:** ❌ Não aprovado no resultado preliminar (19/06). ✅ Recurso enviado (22/06) — aguardando resposta.

---

## Objetivo do Agente

Ao ser acionado neste repositório, seu papel é:

1. **Apoiar a captação de recursos** — identificar editais, transcrever regulamentos, preparar formulários
2. **Organizar documentos** — converter PDFs/DOCX/ODT para .md, catalogar arquivos, manter estrutura padronizada
3. **Manter o site atualizado** — MkDocs Material em `docs/`, deploy via `mkdocs gh-deploy --clean`
4. **Responder aos membros** — linguagem simples e direta, sem jargão técnico desnecessário
5. **Produzir conteúdo** — minutas, ofícios, atas, relatórios e materiais de divulgação

---

## Estrutura do Repositório

```
📂 02_PROPOSTAS/          → Proposta final do Viveiro-Educador
📂 06_CARTOGRAFIA_IMAGENS/ → Mapas e imagens do território
📂 07_DOCUMENTOS_PROJETO/  → Planilha orçamentária (.xlsx)
📂 08_REDES_SOCIAIS/       → Artes para campanhas
📂 09_IDENTIDADE_VISUAL/   → Logos e marca
📂 14_MIDIAS_ASSETS/       → Fotos e mídias
📂 15_EXTRACAO_PDFS/       → PDFs catalogados por assunto
📂 docs/                   → Site MkDocs (fonte)
│  📂 editais/             →   Regulamentos, fichas, formulários
│  📂 projetos/            →   Propostas convertidas (.docx/.odt → .md)
│  📂 documentos_projeto/  →   Atas, formulários, relatórios
│  📂 documentos_administrativos/ → Estatuto, atas de fundação
│  📂 assets/              →   CSS, JS, imagens do site
📄 mkdocs.yml              → Configuração do MkDocs
📄 sentinel_monitor.py     → Monitor de editais
📄 README.md               → Instruções para os membros
```

---

## Ferramentas Disponíveis

| Ferramenta | Função | Status |
|---|---|---|
| **Pandoc** | DOCX/ODT → MD | ✅ |
| **PyMuPDF** (fitz) | Extração de texto de PDFs | ✅ |
| **python-docx** | Leitura/escrita DOCX | ✅ |
| **ffmpeg** (conda) | Conversão de áudio (opus → wav) | ✅ |
| **faster-whisper** | Transcrição de áudio | ✅ | via `conda run -n whisper_env` |
| **pdfplumber** | PDF tabular | ⏳ Pendente (rede) |

**Workaround áudio:** Gateway Telegram já transcreve automaticamente.

---

## Convenções para o Agente

### Documentos
- **Sempre converter** arquivos originais (.docx, .odt, .pdf) para .md antes de versionar
- **NUNCA commitar** arquivos binários grandes (.pdf, .docx, .odt, .jpg, .opus) — vão para TRIAGEM-BRUTA/
- **Nomear arquivos** em português, sem espaços, com hífens: `regulamento-juventude-solidaria.md`
- **Incluir metadados** no topo de cada ficha: fonte, data, contexto

### Editais
Ao processar um novo edital:
1. Baixar PDF do regulamento oficial
2. Converter para .md → `docs/editais/regulamento-<edital>.md`
3. Criar ficha de inscrição → `docs/editais/<edital>/ficha_inscricao.md`
4. Adicionar ao `docs/editais/editais.md` (painel de chamadas)
5. Adicionar navegação no `mkdocs.yml`
6. Build + deploy: `mkdocs gh-deploy --clean`

### Site (MkDocs)
- Tema Material, português-BR
- Após qualquer alteração em `docs/` ou `mkdocs.yml`, rodar `mkdocs gh-deploy --clean`
- Links de documentos usam `https://github.com/.../blob/main/...` (evitar GH Pages para arquivos fora do nav)

### Fluxo de trabalho
1. `git pull` — sincronizar com remoto
2. Fazer alterações
3. `git add <arquivos>`
4. `git commit -m "tipo: descrição concisa"`
5. `git push`
6. `mkdocs gh-deploy --clean` (se alterou docs/)

### Regras críticas
- ❌ NUNCA fabricar citações
- ❌ NUNCA inflar TRL em propostas
- ❌ NUNCA citar documentos internos (prefixos LAB_, ENG_, RES_, SCI_, TAK_) como evidência — só artigos públicos com DOI
- ❌ NUNCA usar termos "biosoberano" ou "protocolos disso/daquilo" em textos públicos
- ✅ Tecnologia Takwara = proposta TRL laboratorial, nunca como aplicada

---

## Repositórios Irmãos

| Repositório | Conteúdo | Público |
|---|---|---|
| `github.com/takwaratec/ECOSALA` | Coletivo de 11 membros — atas, projetos, fichas | Grupo de pesquisa |
| `github.com/takwaratec/fundo-vaga-lumen-2026` | Proposta FINEP Mais Inovação | FINEP/avaliadores |
| `github.com/takwaratec/Analises-e-escrita-cientifica` | Acervo científico — fichas, artigos, TRL | Acadêmico |
| `github.com/takwaratec/plataforma-juventude-solidaria-2026` | **(este repo)** Viveiro-Educador Terra Viva | MST Mário Lago |

---

## Acervo Científico

Para embasar propostas e consultar referências:
👉 https://takwaratec.github.io/Analises-e-escrita-cientifica/

### 🌿 Fichas técnicas relevantes para o Viveiro-Educador

O Acervo Científico da Tecnologia Takwara foi expandido com fichas diretamente aplicáveis ao contexto dos assentamentos e à educação do campo:

| Tema | Ficha | Link |
|---|---|---|
| 🌱 **Fitorremediação com Bambu** | Remediação de solos e águas contaminadas — aplicável a áreas degradadas em assentamentos | [ficha-fitorremediacao-bambu.md](https://github.com/takwaratec/Analises-e-escrita-cientifica/blob/main/docs/analyses/tecnologia-takwara/ficha-fitorremediacao-bambu.md) |
| 🔥 **Bambu e Queimadas na Amazônia** | O papel ecológico do bambu nativo na resiliência ao fogo | [ficha-bambu-queimadas.md](https://github.com/takwaratec/Analises-e-escrita-cientifica/blob/main/docs/analyses/tecnologia-takwara/ficha-bambu-queimadas.md) |
| 🌎 **Ecossistema do Bambu no Brasil** | Distribuição, espécies nativas e exóticas, potencial de manejo | [ficha-ecossistema-bambu-brasil.md](https://github.com/takwaratec/Analises-e-escrita-cientifica/blob/main/docs/analyses/tecnologia-takwara/ficha-ecossistema-bambu-brasil.md) |
| ♻️ **Forno Ecológico Multifuncional** | Pirólise lenta para biochar, pirolenhoso e energia — tecnologia MPTDF | [ficha-forno-ecologico-multifuncional.md](https://github.com/takwaratec/Analises-e-escrita-cientifica/blob/main/docs/analyses/tecnologia-takwara/ficha-forno-ecologico-multifuncional.md) |
| 📦 **Espécies de Bambu no Brasil** | Catálogo de espécies com potencial construtivo e energético | [ficha-especies-bambu-brasil.md](https://github.com/takwaratec/Analises-e-escrita-cientifica/blob/main/docs/analyses/tecnologia-takwara/ficha-especies-bambu-brasil.md) |
| 🌳 **Carbono e Crédito de Carbono** | Sequestro de carbono por florestas de bambu, metodologias VERRA | [ficha-carbono-bambu.md](https://github.com/takwaratec/Analises-e-escrita-cientifica/blob/main/docs/analyses/tecnologia-takwara/ficha-carbono-bambu.md) · [ficha-credito-carbono-bambu.md](https://github.com/takwaratec/Analises-e-escrita-cientifica/blob/main/docs/analyses/tecnologia-takwara/ficha-credito-carbono-bambu.md) |

Acesse o acervo completo em: [github.com/takwaratec/Analises-e-escrita-cientifica/tree/main/docs/analyses/tecnologia-takwara/](https://github.com/takwaratec/Analises-e-escrita-cientifica/tree/main/docs/analyses/tecnologia-takwara/)

---

## Contato

- **Murilo Miguel** — Coordenação do projeto (Coletivo Terra Viva)
- **Fabio Takwara** — Suporte técnico e documentação

---

## Gestão de Frentes de Trabalho

Consulte o arquivo `FRENTES_DE_TRABALHO.md` no repositório mestre (`Mentoria_Tecnologia_Takwara`) para o mapa completo de todas as frentes e regras de fronteira.

---

## Protocolo de Governança (Geral)

Trabalhos de campo com comunidades só após observância das Salvaguardas de Cancún (REDD+).
Referência: [GOV_PROTOCOLO_SEGURANCA_CANCUN.md](https://github.com/takwaratec/Mulheres-Tecem-Amazonia/blob/main/docs/01_GOVERNANCA/GOV_PROTOCOLO_SEGURANCA_CANCUN.md)

---

*AGENTS.md mantido pelo Hermes Agent · Tecnologia Takwara · 2026*
