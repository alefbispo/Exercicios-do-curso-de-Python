'''Escreva um programa que peça um numero e peça pro usuario escolher uma base de converção
1 pra binario
2 pra octal
3 pra hexadecimal'''

numero = int(input('Digite um numero: '))
conversor =  int(input('gostaria de converter {} pra \n'
                       '\033[4:31mBinario = 1\033[m \n'
                       '\033[4:33mOctal = 2\033[m\n'
                       '\033[4:37mHexadecimal = 3\033[m\n'
                       'Digite = '.format(numero)))

if conversor == 1:
    print('O numero {} em binario fica: '.format(numero), bin(numero)[2:])
elif conversor == 2:
    print('O numero {} em octal fica: '.format(numero), oct(numero)[2:])
elif conversor == 3:
    print('O numero {} em hexadecimal fica: '.format(numero), hex(numero)[2:])
else:
    print('Numero invalido!!')