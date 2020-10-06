'''Faça um programa que  leia 6 numeros inteiros
e mostre a soma apenas dos que forem  pares
se o valor for impar desconsidere-o'''

valor = 0
contador = 0
for x in range(1, 6):
    x = int(input('Digite um numero inteiro: '))
    if x % 2 == 0:
        valor += x
        contador += 1
print('Total de numeros pares digitado: {} '.format(contador))
print('O resultado da soma dos valores foi: {}'.format(valor))




