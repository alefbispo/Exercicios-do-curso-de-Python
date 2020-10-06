'''faca um programa  some de todos os numeros impares que sao multiplos de 3
e que se encontram entre 1 e 500'''

acumulador = 0
contador = 0


for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = + 1
        acumulador = + c

print('A soma de todos os {} itens é de: {}'.format(contador, acumulador))