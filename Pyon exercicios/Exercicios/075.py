'''Desenvolva um programa que leia quatro valores
mostre quantas vezes apareceu o numeor 9
 em que posição foi digitado o valor 3
 quais foram os numeros pares'''


v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite outro: '))
v4 = int(input('Digite o ultimo: '))

numeros = (v1, v2, v3, v4)

print(numeros)
if 9 in numeros:
    print(f'O numero 9 apareceu: {numeros.count(9)} vezes')
else:
    print('O valor 9 nao foi digitado')
if 3 in numeros:
    print(f'O valor 3 foi digitado na posição {numeros.index(3)+1}')
else:
    print('O valor 3 nao foi digitado')
print('Voce digitou ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
