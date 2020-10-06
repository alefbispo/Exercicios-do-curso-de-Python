'''faça um programa pra jogar par ou impar com o computador
o jogo so sera interrompido quando o jogador perder
mostrando quantas vezes ele venceu ao final o programa'''

from random import randint
resultado = 0
contador = 0

while True:
    par_impar = str(input('\033[4:31mEscolha par ou impar\033[m\n'
                          '\033[0:33m[ P ] / [ I ] : \033[m')).upper().strip()[0]

    jogada =  int(input('Escolha um numero: '))

    computador = randint(1, 11)
    resultado = computador + jogada

    print('=' * 20)
    print(f'Voce jogou {jogada} e o computador jogou {computador}')
    print('=' * 20)

    if resultado % 2 == 0 and par_impar == "P":
        print('*' * 20)
        print(f'deu ({par_impar}) \033[0:32mVOCE GANHOU PARABENS!!\033[0:32m')
        print('*' * 20)
        contador += 1
    else:
        print('\033[0:31mVoce perdeu\033[0:31m... que pena :(')
        break
print('='*20)
print(f'\033[0:33mVoce ganhou {contador} vezes!\033[0:33m')
print('='*20)
