'''Peça o ano de nascimento  e informe de acordo com a idade:
se ele ainda vai se alistar ao serviço militar
se é hora de se alistar
ou se ja passou o tempo
tbm deve mostar o tempo que falta ou o tempo que ja passou'''

from datetime import date

sexo = int(input('''Qual seu sexo?
[1] pra masculino
[2] pra feminino
digite:  '''))
if sexo == 2:
    print('Alistamento é obrigatorio apenas para homens!')
    exit()
else:
    ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
comparacao = ano_atual - ano

if comparacao == 18:
    print('Ja esta na hora de se alistar!!')
elif comparacao < 18:
    print('Ainda esta muito cedo pra se alistar, ainda falta {} anos'.format(18 - comparacao))
elif comparacao > 18:
    print('Ja se passaram {} anos do tempo de  se alistar!'.format(comparacao - 18))

