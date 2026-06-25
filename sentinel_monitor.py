#!/usr/bin/env python3
"""
Sentinel Script — MST Mario Lago / Juventude Solidaria
Monitoramento de Editais e Geracao de Fichas de Inscricao

FLUXO OBRIGATORIO PARA CADA EDITAL:
1. BAIXAR o PDF do regulamento para TRIAGEM-BRUTA/05_EDITAIS_REGULAMENTOS/
2. CONVERTER o regulamento para .md em docs/editais/[edital]/regulamento.md
3. CONVERTER documentos de apoio e formulario oficial para .md
4. ANALISAR compativelidades (TRL, valores, prazos, contrapartida)
5. ESCREVER orientacoes no boletim semanal
"""

import os

CAMINHOS = {
    "regulamentos": "TRIAGEM-BRUTA/05_EDITAIS_REGULAMENTOS/",
    "editais_docs": "docs/editais/",
}


def baixar_regulamento(url, edital_nome):
    """Passo 1: Baixar o PDF do regulamento para a pasta de triagem."""
    destino = os.path.join(CAMINHOS["regulamentos"], f"{edital_nome}_regulamento.pdf")
    print(f"[1/5] Baixar regulamento de: {url}")
    print(f"      Salvar em: {destino}")
    print(f"      Status: PENDENTE (executar manualmente ou via wget/curl)")
    return destino


def converter_para_md(arquivo_pdf, edital_nome):
    """Passo 2: Converter o PDF do regulamento para .md usando textutil (macOS) ou pypdf."""
    destino_md = os.path.join(CAMINHOS["editais_docs"], f"{edital_nome}_regulamento.md")
    print(f"[2/5] Converter PDF para .md:")
    print(f"      De: {arquivo_pdf}")
    print(f"      Para: {destino_md}")
    print(f"      Comando: textutil -convert txt -output /tmp/{edital_nome}.txt {arquivo_pdf}")
    print(f"      Status: PENDENTE")
    return destino_md


def converter_formulario_edital(arquivo_original, edital_nome):
    """Passo 3: Converter o formulario oficial de inscricao para .md."""
    destino = os.path.join(CAMINHOS["editais_docs"], f"{edital_nome}_formulario.md")
    print(f"[3/5] Converter formulario oficial para .md:")
    print(f"      De: {arquivo_original}")
    print(f"      Para: {destino}")
    print(f"      Status: PENDENTE")
    return destino


def analisar_regulamento(edital_nome):
    """Passo 4: Extrair e verificar requisitos criticos do regulamento."""
    print(f"\n[4/5] ANALISE DE REGULAMENTO: {edital_nome}")
    print("=" * 50)
    print("[ ] TRL minima exigida: _____")
    print("[ ] Valor minimo: R$ _____")
    print("[ ] Valor maximo: R$ _____")
    print("[ ] Contrapartida minima: _____%")
    print("[ ] Prazo de execucao maximo: _____ meses")
    print("[ ] Documentos obrigatorios:")
    print("      - [ ] Anexo 3 — Declaracao de acoes coletivas")
    print("      - [ ] Anexo 4 — Declaracao ambiental")
    print("      - [ ] Anexo 5 — Metodologia TRL")
    print("      - [ ] Outros: _____")
    print("[ ] Criterios eliminatórios identificados? [ ] SIM [ ] NAO")
    print("[ ] Criterios classificatórios identificados? [ ] SIM [ ] NAO")
    print("=" * 50)

    # Verificar compativelidade com o perfil do Coletivo Terra Viva
    print("\nCOMPATIBILIDADE COM O COLETIVO:")
    print(f"[ ] Proponente pode ser o Coletivo Terra Viva?")
    print(f"[ ] Valor dentro da capacidade de contrapartida?")
    print(f"[ ] Prazo compativel com a disponibilidade da equipe?")
    print(f"[ ] Escopo alinhado ao Viveiro-Educador / SAFs / Bambu?")
    return {}


def gerar_boletim_semanal(editais_analisados):
    """Passo 5: Escrever o boletim semanal com orientacoes."""
    boletim = f"""# Boletim Sentinel — Semana {__import__('datetime').date.today().strftime('%d/%m/%Y')}

> Opotunidades de fomento mapeadas e analisadas.

## Editais Ativos

"""
    for e in editais_analisados:
        boletim += f"""---
### {e['nome']}

**Situacao:** {e['status']}
**Prazo:** {e['prazo']}
**Valor:** {e['teto']}
**Compatibilidade:** {e['compativel']}
**Orientacao:** {e['orientacao']}

"""
    return boletim


if __name__ == '__main__':
    print("=" * 60)
    print("  SENTINEL MST MARIO LAGO — MONITORAMENTO DE EDITAIS")
    print("  Fluxo obrigatorio de 5 passos para cada edital")
    print("=" * 60)

    # Simulacao para o edital mais urgente
    edital = "Fundo Casa — Juventudes e Justica Climatica"

    print(f"\n>>> PROCESSANDO: {edital} <<<\n")

    # Passo 1
    baixar_regulamento(
        "https://www.fundocasa.org.br/editais/juventudes-clima",
        "fundo-casa-juventudes-clima-2026"
    )

    # Passo 2 e 3
    converter_para_md(
        "TRIAGEM-BRUTA/05_EDITAIS_REGULAMENTOS/fundo-casa-juventudes-clima-2026_regulamento.pdf",
        "fundo-casa-juventudes-clima-2026"
    )
    converter_formulario_edital(
        "TRIAGEM-BRUTA/05_EDITAIS_REGULAMENTOS/fundo-casa-juventudes-clima-2026_formulario.pdf",
        "fundo-casa-juventudes-clima-2026"
    )

    # Passo 4
    analisar_regulamento(edital)

    # Passo 5
    print("\n[5/5] BOLETIM SEMANAL GERADO:")
    boletim = gerar_boletim_semanal([
        {
            "nome": edital,
            "status": "REGULAMENTO NAO ANALISADO",
            "prazo": "30/jun/2026",
            "teto": "R$ 60.000,00",
            "compativel": "PENDENTE DE ANALISE",
            "orientacao": "Baixar regulamento, converter para .md e analisar requisitos antes de preencher."
        }
    ])
    print(boletim)
