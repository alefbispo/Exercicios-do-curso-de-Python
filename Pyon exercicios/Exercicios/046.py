'''Faça um programa que mostre na tela uma contagem regressiva
indo de 10 até 0
com pausa de 1s'''
from time import sleep

print('**', 'CONTAGEM REGRESSIVA!!', '**')
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('FILIZ ANO NOVO!!!')