# 4 - Crie um programa que tenha a função leiaInt(),que vai funcionar de forma semelhante a função input( ) do python,
#só que fazendo a validação para aceitar apenas um valor númerico


def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, digite um valor inteiro válido.")

# Exemplo de uso da função
numero = leiaInt("Digite um número inteiro: ")
print("Você digitou:", numero)

