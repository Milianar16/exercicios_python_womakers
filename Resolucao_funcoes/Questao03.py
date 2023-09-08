# 3 - Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius
# para Fahrenheit e vice-versa . Para cada opção, crie uma função. crie uma terceira, que é um menu
#para o usuário escolher  a opção desejada, esse menu chama a função de conversão-correta

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu_conversao():
    print("Escolha uma opção:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius é igual a {resultado:.2f} graus Fahrenheit.")
    elif escolha == 2:
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit é igual a {resultado:.2f} graus Celsius.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    menu_conversao()
