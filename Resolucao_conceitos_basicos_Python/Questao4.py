'''
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do
seu salário no referido mês.

'''

# Solicita o valor da taxa horária e converte para float
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))

# Solicita o número de horas trabalhadas no mês e converte para float
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário mensal multiplicando o valor por hora pelas horas trabalhadas
salario_mensal = valor_por_hora * horas_trabalhadas

# Mostra o resultado do salário mensal
print(f"Seu salário mensal é: R${salario_mensal:.2f}")
