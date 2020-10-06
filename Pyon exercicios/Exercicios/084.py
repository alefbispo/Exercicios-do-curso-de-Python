"""Faça um progrma que leia o peso e idade de varias pessoas
e guarde em uma lista
mostre
quantas pessoas foram cadastradas
uma lista com as pessoas mais pesadas (+100kg)
uma lista com as pessoas mais leves (- 70kg)"""
lista  = []
dados = []
resposta = 'S'
contador  = 0
while resposta == 'S':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    contador += 1
    resposta = input('Continuar: [S/N]: ').upper()[0]
    if resposta == 'N':
        break

print(f'{contador} pessoas foram cadastradas.')
for peso in lista:
    if peso[1] >= 100:
        print(f'{peso[0]} tem peso superior a 100kg')
    if peso[1] <= 70:
        print(f'{peso[0]} tem peso inferior a 70kg')





