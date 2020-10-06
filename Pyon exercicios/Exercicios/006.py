#peça um numero e mostre o dobro o triplo e sua raiz quadrada
n1 = int(input('Digite um numero: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print('O numero é: {}\n o dobro é: {}\n o triplo é: {}\n a raiz quadrada é: {:.3}'.format(n1, dobro, triplo, raiz))

