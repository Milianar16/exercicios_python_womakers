
    #2 -  Programa nome ao contrário em maipusculas.
    #Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente
    #utilizando somente letras maiúsculas
    #Dica: lembre-se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.



def exercicio_02():
     nome = input("Digite seu nome: ")

     letras = []
     for i in range(len(nome)-1, -1, -1):
         letras.append(nome[i].upper())

         print(''.join(letras))

exercicio_02()
