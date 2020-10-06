'''Crie um programa que gera 5 numeros aleatorios e guarda em uma tupla
depois mostre a lsita de numeros gerados
indique o menor
e o maior'''
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('A lista é : ', end='')
for x in numeros:
    print(x, end=' ')

print(f'\nE o maior numero é {max(numeros)} e o menor é {min(numeros)}')
