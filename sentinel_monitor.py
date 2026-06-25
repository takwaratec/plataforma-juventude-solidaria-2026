#!/usr/bin/env python3
"""
Sentinel Script — MST Mario Lago / Juventude Solidaria
Monitoramento de Editais e Geracao de Fichas de Inscricao
Foco: Viveiro-Educador, juventude assentada, agroecologia, SAFs, bioconstrucao com bambu
"""

def formatar_ficha_inscricao(edital_nome, teto, prazo, eixos):
    template = f"""# Gabarito de Inscricao: {edital_nome}
**Teto:** {teto} | **Prazo:** {prazo}
**Eixos:** {', '.join(eixos)}

## [CAMPO 1] IDENTIFICACAO DO PROJETO
- Titulo: [Inserir]
- Proponente: Coletivo Terra Viva / [Interveniente financeiro]
- Contato: Murilo Miguel (Setor de Juventude - MST)
- Territorio: Assentamento Mario Lago, Ribeirao Preto/SP (APA Aquifero Guarani)

## [CAMPO 2] JUSTIFICATIVA E DIAGNOSTICO
450 familias assentadas em transicao agroecologica. Alta evasao juvenil por falta de renda e qualificacao.
Incendios criminosos de 2024 devastaram reservas legais. Tecnologias de toxicidade zero para protecao do
Aquifero Guarani. Viveiro-Educador como estrategia de formacao, renda e permanencia no campo.

## [CAMPO 3] METODOLOGIA
Fase 1: Mobilizacao e aquisicao de materiais
Fase 2: Mutirao de bioconstrucao com bambu tratado (MPTDF)
Fase 3: Formacao de jovens viveiristas e producao de mudas
Fase 4: Comercializacao e cooperativismo

## [CAMPO 4] METAS
- Meta 1: Infraestrutura instalada
- Meta 2: 10 jovens capacitados
- Meta 3: Producao e doacao de mudas
- Meta 4: Modelo replicavel para os 4 assentamentos da regional
"""
    return template

def gerar_boletim(editais):
    boletim = "# Boletim Sentinel — MST Mario Lago\n"
    boletim += f"> Gerado automaticamente | {len(editais)} oportunidades ativas\n\n"
    for i, e in enumerate(editais, 1):
        boletim += f"---\n### {i}. {e['nome']}\n"
        boletim += f"**Teto:** {e['teto']} | **Prazo:** {e['prazo']}\n"
        boletim += f"**Eixos:** {', '.join(e['eixos'])}\n"
        boletim += f"{e['descricao']}\n\n"
    return boletim

if __name__ == '__main__':
    # Mapeamento de oportunidades ativas para o Coletivo Terra Viva
    editais = [
        {
            "nome": "Juventudes e Justica Climatica — Fundo Casa",
            "teto": "R$ 60.000,00",
            "prazo": "30/jun/2026",
            "eixos": ["Juventude", "Clima", "Agroecologia", "SAFs"],
            "descricao": "Ampliacao do Viveiro-Educador para centro comunitario. Expansao de 4mx8m para escala maior. Bolsas para jovens viveiristas."
        },
        {
            "nome": "Chamada Simplificada — Fundo Casa",
            "teto": "R$ 20.000,00",
            "prazo": "14/jul/2026",
            "eixos": ["Bioconstrucao", "Bambu", "MPTDF"],
            "descricao": "Implantacao do Forno Ecologico MPTDF. Bombonas 200L, panela 30L, Rocket Stove, ferramentas."
        },
        {
            "nome": "Juventude Solidaria 02/2026",
            "teto": "R$ 12.000,00",
            "prazo": "A confirmar",
            "eixos": ["Juventude", "Formacao", "Viveiro"],
            "descricao": "Projeto Viveiro-Educador ja submetido. Aguardando novo ciclo."
        }
    ]

    print("=== SENTINEL MST — MONITORAMENTO DE EDITAIS ===")
    print(gerar_boletim(editais))

    # Gerar gabarito para o edital mais urgente
    print("\n=== GABARITO: Edital com prazo mais proximo ===")
    gab = formatar_ficha_inscricao(editais[0]["nome"], editais[0]["teto"],
                                    editais[0]["prazo"], editais[0]["eixos"])
    print(gab[:300])
