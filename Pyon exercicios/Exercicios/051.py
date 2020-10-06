'''Desenvolva um programa que leia o primeiro termo de uma progressao aritimetica e o termo'''
termo = int(input('Contar ate qual numero? '))
progressao = int(input('Pular de quanto em quanto? '))
decimo = termo + (10 - 1) * progressao

for n in range(termo, decimo + progressao, progressao):
    print(n, end=' > ')
print('Finish')