import numpy as np

def calcular_fcff(ebit, taxa_imposto, depreciacao, capex, variacao_capital_giro):
    return ebit * (1 - taxa_imposto) + depreciacao - capex - variacao_capital_giro


def calcular_dcf(fcff_inicial, crescimento, wacc, crescimento_terminal, anos=5):
    fluxos = []

    for ano in range(1, anos + 1):
        fcff = fcff_inicial * (1 + crescimento) ** ano
        fluxos.append(fcff / ((1 + wacc) ** ano))

    valor_terminal = (fcff * (1 + crescimento_terminal)) / (wacc - crescimento_terminal)
    valor_terminal_descontado = valor_terminal / ((1 + wacc) ** anos)

    valor_empresa = sum(fluxos) + valor_terminal_descontado

    return valor_empresa


def calcular_preco_justo(valor_empresa, divida_liquida, numero_acoes):
    valor_equity = valor_empresa - divida_liquida
    return valor_equity / numero_acoes
