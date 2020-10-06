'''Crie um jokenpo'''

from random import randint
from time import sleep

print('**' * 15)
print('''Para jogar Digite: 
[0] pra pedra
[1] pra tesoura
[2] pra papel''')
print('**' * 15)
jogada = int(input('Sua jogada: '))
if jogada >= 3:
    print('JOGADA INVALIDA')
    exit()

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Poo!')
sleep(1)

lista = ('Pedra', 'Tesoura', 'Papel')
computador = randint(0, 2)
print('=-' * 15)
sleep(0.5)
print('''O computador jogou {} 
E voce jogou {}'''.format(lista[computador], lista[jogada]))
sleep(0.5)
print('=-' * 15)
sleep(0.5)

if computador == 0:
    if jogada == 0:
        print('Deu empate!')
    elif jogada == 1:
        print('Computador ganhou!')
    elif jogada == 2:
        print('Jogador ganhou!')

if computador == 1:
    if jogada == 0:
        print('Jodaor ganhou!')
    elif jogada == 1:
        print('Deu empate!')
    elif jogada == 2:
        print('Computador ganhou!')


if computador == 2:
    if jogada == 0:
        print('Computador ganhou!')
    elif jogada == 1:
        print('Jogador ganhou!')
    elif jogada == 2:
        print('Deu empate!')

'''if jogada == computador:
    print('Empate')
elif jogada == 1 and computador == 2:
    print('Voce ganhrou!')
elif jogada == 1 and computador == 3:
    print('Voce perdeu!')
elif jogada == 2 and computador == 1:
    print('Voce perdeu!')
elif jogada == 2  and computador == 3:
    print('Voce ganhou')'''
