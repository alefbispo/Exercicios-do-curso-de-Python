#leia 3 numero e mostre o maior e o menor

n1 = int(input('Digite um numero: '))
n2 = int(input('Difite o segundo muero: '))
n3 = int(input('Digite o terceiro numero: '))

maior = n1
menor = maior

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3


if n2 > maior:
    menor = n2
if n3 < maior:
    menor = n3

print('O maior numero é: {} e o menor é: {}.'.format(maior, menor))
