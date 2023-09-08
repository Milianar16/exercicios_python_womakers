def exercicio_01a():
 '''
  Crie um programa que leia quanto dinheiro uma pessoa tem na carteira,
  e calcule quanto poderia comprar de cada moeda estrangeira.
  Considere a tabela de conversão abaixo:

   Dólar americano: $4,91
   Peso Argentino: $ 0,02
   Dólar Australiano: $3,18
   Dólar Canadense: $3,64
   Franco Suiço: $0,42
   Euro: $ 5,36
   Libra esterlina: $ 6,21
 '''
#valor = input('Digite o valor em reais: ') # fazer com cada moeda
#print(f'Dólar Americano: {float(valor)/4.91}')


def exercicio_01b():
    valor = input('Digite o valor em reais: ')
    moedas = {
   "Dolar Americano": 4.91,
   "Peso Argentino": 0.02,
   "Dólar Australiano": 3.18,
   "Dólar Canadense": 3.64,
   "Franco Suiço": 0.42,
   "Euro": 5.36,
   "Libra esterlina": 6.21
}
    for moeda, valor_moeda in moedas.items():
        print(f'{moeda}: {float(valor)/valor_moeda}')

exercicio_01b()
