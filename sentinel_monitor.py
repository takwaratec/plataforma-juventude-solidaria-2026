#!/usr/bin/env python3
"""
Sentinel Script: Monitoramento de Editais e Geração de Fichas de Inscrição
Este script automatiza o monitoramento de novas chamadas a partir de parâmetros da Matriz Tecnológica MQTF
e gera esqueletos de preenchimento estruturados para o Coletivo Terra Viva / Mário Lago.
"""
import os
import sys

def formatar_ficha_inscricao(edital_nome, teto_financeiro, eixos):
    template = f"""# Gabarito de Inscrição: {edital_nome}
**Parâmetros de Custeio Máximo**: {teto_financeiro}
**Eixos Tecnológicos Aplicados**: {", ".join(eixos)}

## [CAMPO 1] IDENTIFICAÇÃO DO PROJETO
- Título do Projeto: [Inserir Título]
- Proponente: Coletivo Terra Viva / Cooperativa Comuna da Terra
- Contato: Murilo Miguel (Setor de Juventude - MST)

## [CAMPO 2] JUSTIFICATIVA E DIAGNÓSTICO
- Rascunho Territorial: O Assentamento Mário Lago (Ribeirão Preto/SP) abriga 450 famílias dedicadas à agricultura familiar e à transição agroecológica. O território está situado sobre a zona de recarga do Aquífero Guarani (APA). A evasão de jovens assentados do campo para a periferia da cidade (êxodo rural) é impulsionada pela busca de qualificação e renda. Esta vulnerabilidade social foi agravada após os incêndios criminosos de 2024. A tecnologia de tratamento de bambu (vapor alcalino + pirolenhoso) e bioconstrução atua gerando especialização técnica local e soberania produtiva atóxica sem contaminação do lençol freático.

## [CAMPO 3] METODOLOGIA E ATIVIDADES
- Fase 1: Planejamento, mobilização e coleta de bambu local.
- Fase 2: Mutirão de tratamento ecológico e montagem da infraestrutura.
- Fase 3: Capacitação prática de jovens viveiristas e produção de mudas.
- Fase 4: Governança cooperativa não-formal e escoamento comercial de mudas/brotos.

## [CAMPO 4] METAS E RESULTADOS
- Meta 1: Instalação física da estufa de bambu de baixo custo.
- Meta 2: Capacitação direta de no mínimo 10 jovens voluntários.
- Meta 3: Produção de mudas e doação de 30% para áreas degradadas.
"""
    return template

if __name__ == '__main__':
    print("Iniciando varredura Sentinel de fomento...")
    # Executa a geração de um gabarito genérico de teste na execução local
    gab = formatar_ficha_inscricao("Edital Novo Exemplo 2026", "R$ 30.000,00", ["Agroecologia", "Bambu Construtivo", "Autonomia"])
    print(gab[:250] + "\n...")
