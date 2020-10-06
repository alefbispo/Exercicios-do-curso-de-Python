'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
from  math import factorial
numero = int(input('Digite um numero: '))
fatorial = numero

print('Fatorial de {}!\n '.format(numero), end='')
while numero > 0:
    print('{}'.format(numero), end='')
    print(' x ' if numero > 1 else ' = ', end='')
    numero -= 1
print(factorial(fatorial), end='')
