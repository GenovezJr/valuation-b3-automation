from dcf import calcular_fcff, calcular_dcf, calcular_preco_justo

print("=== VALUATION B3 AUTOMATIZADO ===")

ebit = float(input("EBIT: "))
taxa_imposto = float(input("Taxa de imposto (ex: 0.34): "))
depreciacao = float(input("Depreciação: "))
capex = float(input("CAPEX: "))
variacao_capital_giro = float(input("Variação Capital de Giro: "))
divida_liquida = float(input("Dívida Líquida: "))
numero_acoes = float(input("Número de ações: "))
crescimento = float(input("Crescimento projetado (ex: 0.05): "))
wacc = float(input("WACC (ex: 0.10): "))
crescimento_terminal = float(input("Crescimento terminal (ex: 0.03): "))

fcff = calcular_fcff(ebit, taxa_imposto, depreciacao, capex, variacao_capital_giro)

valor_empresa = calcular_dcf(fcff, crescimento, wacc, crescimento_terminal)

preco_justo = calcular_preco_justo(valor_empresa, divida_liquida, numero_acoes)

print(f"\nPreço Justo estimado: R$ {preco_justo:.2f}")
