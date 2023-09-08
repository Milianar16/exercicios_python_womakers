def exercicio_01():
    '''
1 - Faça um programa que peça as quatro notas de 10 alunos,
calcuçe e armazene numa lista a média de cada aluno,
imprima o número de alunos com média maior ou  igual a 7.0
'''

listaNotas = []
listaMedias = []

quatidadeAlunos = 10
quatidadeNotas = 4

#loop para coletar as notas e calcular as médias
# range gera uma lista de 10 até 0
# append vai incluir o item no fim da lista

for aluno in range(quatidadeAlunos):
    listaNotas.append([])
    for nota in range(quatidadeNotas):
        listaNotas[aluno].append(
            float(
                input(f'Digite a nota {nota+1} do  aluno {aluno+1}: ')
            )
        )

        for notas in listaNotas:
            listaMedias.append(

              sum(notas) / len(notas)
            )

    alunos_aprovados= sum(1 for media in listaMedias if media >= 7)

print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")

exercicio_01()
