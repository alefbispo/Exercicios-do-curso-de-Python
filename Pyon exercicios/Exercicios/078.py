"""Faça um programa que leia 5 valores numericos e guarde em uma lista
no final mostre qual o maior e o meor valos e qual sua posição da lista"""
valor = []

for c in range(0, 5):
    valor.append(input('Digite um valor: '))

print(f'Itens salvos {valor}')
print(f'O maior valor é {max(valor)} e sua posição é :', end=' ')
for loc, n in enumerate(valor):
    if max(valor) == n:
        print(f'{loc}...', end=' ')
print()

print(f'O menor valor é {min(valor)} e esta na posição: ', end=' ')
for local, numero in enumerate(valor):
    if min(valor) == numero:
        print(f'{local}...', end=' ')
