#faça um programa que peça o nome completro e uma pessoa e mostre o primeiro e o ultimo nome

a = input('Digite seu nome completo: ').strip().split()

print(f'O primeiro nome é: {a[0]}, e o ultimo nome é: {a[-1]}')
