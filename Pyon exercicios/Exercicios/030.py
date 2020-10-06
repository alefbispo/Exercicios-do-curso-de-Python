#crie um programa que leia um numero e diga se ele é par ou impar

num = int(input('Digite um numero: '))
resto = num % 2

if resto >= 1:
    print('O numero é  impar')
else:
    print('O numero é par')

