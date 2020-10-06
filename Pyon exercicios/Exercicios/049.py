'''Faça tabuala usando o  laço for'''

valor = int(input('Quer saber a tabuada de qual valor??  '))

print('=-' * 10)
print('TABUADA')
print('=-' * 10)

for x in range(1, 11):
    print('{} x {} = {}'.format(valor,x, valor*x))
