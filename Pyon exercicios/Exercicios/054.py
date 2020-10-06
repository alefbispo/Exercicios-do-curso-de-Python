'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0

for x in range(1, 8):
    ano = int(input('Ano de nascimento: '))
    if ano_atual - ano >= 21:
        maior += 1
       # print('Ja é maior de idade!')
    else:
        menor += 1
       # print('Menor de idade!')
print('Temos {} maiores de idade \nE {} maior de idade!'.format(maior, menor))