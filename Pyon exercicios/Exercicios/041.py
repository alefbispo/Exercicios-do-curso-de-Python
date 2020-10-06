'''A confederação de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria de acordo com sua idade
ate 9 anos mirim
ate 14 anos infantil
ate 19 anos junior
ate 20 anos senior
acima master'''

from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
comparacao = ano_atual - ano

if comparacao < 9:
    print('O atleta tem {} anos classificação MIRIM'.format(comparacao))
elif comparacao < 14:
    print('O atleta tem {} anos, categoria INFANTIL'.format(comparacao))
elif comparacao < 19:
    print('O atleta tem {} anos, categoria JUNIOR'.format(comparacao))
elif comparacao < 20:
    print('O atleta tem {} anos, categoria SENIOR'.format(comparacao))
elif comparacao > 20:
    print('O atleta tem {} anos, categoria MASTER'.format(comparacao))