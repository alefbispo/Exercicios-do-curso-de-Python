'''Faça um pgrograma que leia um numero e diga se ele é ou nao um numero primo'''

numero = int(input('Digite um numero: '))
total = 0

for x in range(1, numero + 1):
    if numero % x == 0:
        total += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(x), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(numero, total))
if total == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele nao é primo!')
