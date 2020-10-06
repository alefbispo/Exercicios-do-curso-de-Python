'''Melhore o jogo do DESAFIO 28
onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

numero = randint(0, 10)
palpite = int(input('Chute um numero de 1 a 10: '))
tentativas = 1

while palpite != numero:
    if numero < palpite:
        print('Menos...')
    if numero > palpite:
        print('Mais...')
    palpite = int(input('Palpite errado!, tente novamente!\n'
                        'Chute um numero de 1 a 10: '))
    print('=================================')
    tentativas = tentativas + 1
print('=====  VOCÊ VENCEU!!! =====')
print('PARABENS!! Voce venceu! e precisou de {} tentativas!'.format(tentativas))