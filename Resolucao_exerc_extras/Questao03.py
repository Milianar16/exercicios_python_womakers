
    #Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, se o salário for
    # até 1000,00 o funcionário terá 20% de aumento
    # Entre 1001,00 até 2800,00 o funcionário terá 10% de aumento
    #Acima de 2801,00 o funcionário terá 5% de aumento

def calcular_novo_salario(salario_atual):
    if salario_atual <= 1000.00:
        aumento = salario_atual * 0.20  # 20% de aumento
    elif salario_atual <= 2800.00:
        aumento = salario_atual * 0.10  # 10% de aumento
    else:
        aumento = salario_atual * 0.05  # 5% de aumento

    novo_salario = salario_atual + aumento
    return novo_salario

salario_atual = float(input("Digite o salário atual do funcionário: "))

novo_salario = calcular_novo_salario(salario_atual)

print(f"O novo salário é: R${novo_salario:.2f}")


