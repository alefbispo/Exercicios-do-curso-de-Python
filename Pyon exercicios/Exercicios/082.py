"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""
lista1 = []
lista2 = []
lista3 = []
v = 1
sair = 'S'
while sair == 'S':
    valor = int(input(f'Digite o {v}° valor: '))
    v += 1
    lista1.append(valor)
    sair = str(input('Adicionar mais valores?? [S/N]: ')).upper()[0]
    if sair == 'N':
        print('Saindo do loop...')
        break

for posicao, item in enumerate(lista1):
    if item % 2 == 0:
        lista2.append(item)
    else:
        lista3.append(item)
print('Lista completa: ', lista1)
print('Lista com pares: ', lista2)
print('Lista com impares: ', lista3)
