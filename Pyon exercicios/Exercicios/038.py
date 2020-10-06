'''Escreva um programa que leia dois numero e compareos
dizendo se um é maior que o outro
ou se os numero sao iguais'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('{} é maior que {}!!'.format(n1, n2))
elif n1 < n2:
    print('{} é maior que {}'.format(n2, n1))
elif n1 == n2:
    print('Os numeros são iguais!')