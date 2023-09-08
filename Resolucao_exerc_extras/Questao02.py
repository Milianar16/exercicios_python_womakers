# 2- Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
#de dias pelos quais eles foram alugados. Calcule o preço a pagar, sabendo  que o carro custa 80,00 por dia e 0,20 por km rodado.

def calcular_preco_aluguel(km_percorridos, dias_alugados):
    preco_por_dia = 80.00
    preco_por_km = 0.20

    custo_dias = dias_alugados * preco_por_dia
    custo_km = km_percorridos * preco_por_km

    preco_total = custo_dias + custo_km

    return preco_total

km_percorridos = float(input("Quantos quilômetros foram percorridos? "))
dias_alugados = int(input("Por quantos dias o carro foi alugado? "))

preco_a_pagar = calcular_preco_aluguel(km_percorridos, dias_alugados)

print(f"O preço a pagar é: R${preco_a_pagar:.2f}")
