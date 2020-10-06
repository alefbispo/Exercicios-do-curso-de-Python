"""Crie um programa que o usuario possa digitar varios valores em uma lista
caso o numero ja exista la dentro ele n sera adicionado
no final sera exibido todos os valores em ordem crescente"""
resposta = 'S'
lista = []

while resposta != 'N':
    num = (input('Digite um valor: '))
    if num in lista:
        print('Valor nao adicionado..')
    else:
        lista.append(num)
    resposta = input('Quer continuar? [ s ] / [ n ]: ').upper()

print(f'A lista normal é {lista}')
lista.sort()
print(f'A lista em ordem crescente é {lista}')
