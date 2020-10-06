#peca um ano e diga se o ano é bisexto
from  datetime import date
ano = int(input('Digite um ano: '))

resto_quatro = ano % 4
resto_cem = ano % 100
if ano == 0:
   ano = date.today().year
if resto_quatro == 0 and resto_cem > 0:
    print('Ano {} é bisexto'.format(ano))
else:
    print('{} Não é bisexto'.format(ano))