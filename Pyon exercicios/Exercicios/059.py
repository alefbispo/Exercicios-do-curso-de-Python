'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
escolha = 0
valor_1 = int(input('Digite um valor 1: '))
valor_2 = int(input('Digite o valor 2: '))

while escolha != 5:
    escolha = int(input('[ 1 ] somar\n'
                        '[ 2 ] multiplicar\n'
                        '[ 3 ] maior\n'
                        '[ 4 ] novos números\n'
                        '[ 5 ] sair do programa\n'
                        'Escolha: '))

    if escolha != (1, 5):
        print('=-' * 10)
        print('Escolha invalida!')
        print('=-' * 10)
        sleep(1)

    if escolha == 1:
        print('A soma de {} com {} é: {}'.format(valor_1, valor_2, valor_1 + valor_2))
        print('=-' * 10)
        sleep(1)

    if escolha == 2:
        print('=-' * 10)
        print('A multiplicação de {} com {} é: {}'.format(valor_1, valor_2, valor_1 * valor_2))
        print('=-' * 10)
        sleep(1)

    if escolha == 3:
        print('=-' * 10)
        if valor_1 > valor_2:
            print('O maior numeor é : {} '.format(valor_1))
            sleep(1)
        else:
            valor_2 > valor_1
            print('O maior numeor é : {}'.format(valor_2))
        print('=-' * 10)
        sleep(1)

    if escolha == 4:
        print('=-' * 10)
        valor_1 = int(input('Digite um valor 1: '))
        valor_2 = int(input('Digite o valor 2: '))
        print('=-' * 10)
        sleep(1)

    if escolha == 5:
        print('=-' * 10)
        print('Saindo...')
        print('=-' * 10)
        sleep(1)
        exit()


