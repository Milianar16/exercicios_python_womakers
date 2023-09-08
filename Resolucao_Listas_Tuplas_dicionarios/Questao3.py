
    # #3 - Escreva um programa Python onde todos os valores em um dicionário são emitidos
    # Se sim, imprima True. Caso contrário, imprima False

dicionario = {"banana": 'fruta', 'casa': 'imovél', 'laranja': 'fruta'}
print(dicionario)

valores_emitidos = all(valor  for valor in dicionario.values())

if valores_emitidos:
    print('True')
else:
    print('False')



