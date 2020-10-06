#peça o nome completo e mostre
#o nome com todas as letras maiusculas
#o nome com todas as minusculo
#quastas letras sao ao ttodo sem considerar espço
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
cortado = nome.split()
espaco = nome.replace(' ', '')

print('ANALISANDO...')
print(f'O nome é: {nome}')
print('Todo em maiusculo: ', nome.upper())
print('Todo em minusculo: ', nome.lower())
print(f'O nome tem : {len(espaco)} letras')
print(f'O primeiro nome é {cortado[0]} e tem', len(cortado[0]), 'letras')

