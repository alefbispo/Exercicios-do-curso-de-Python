#faça o computador "pensar" um numero entre 0 e 5
# e peça pro usuario tentar descobir o resultado
#o programa deve dizer se o usuario venceu ou perdeu
from random import randint
n = int(randint(0, 5))
t = int(input('Tente advinhar o numero entre 0 a 5: '))

if t == n:
    print('Acertou mizeravi!!! PARABENS')
else:
    print('Errou mizeravelmente ....')
print('O numero era {}'.format(n))