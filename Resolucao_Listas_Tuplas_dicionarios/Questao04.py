'''
4."Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
"Já trabalhou com a vítima?"
"O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como""Suspeita"",
entre 3 e 4 como""Cúmplice""e 5 como""Assassino"".Caso contrário,ele será classificado
como""Inocente"".
'''
respostas_positivas = 0

perguntas = [
"Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?"
]

for pergunta in perguntas:
    resposta = input( pergunta + "(Sim/Não): ").lower()
    if resposta == "sim":
        respostas_positivas += 1

    if respostas_positivas == 5:
        classificacao = "Assassino"
    elif respostas_positivas >= 3:
        classificacao = "Cúmplice"
    elif respostas_positivas >=2:
        classificacao = "Suspeito"
    else:
        classificacao = "Inocente"

    print(f'Classificação: {classificacao}')
