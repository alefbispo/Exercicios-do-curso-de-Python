#peca a medida em metros e converta em centimetros e milimetros

v1 = float(input('Digite um valor em metros: '))
centimetro = v1 * 100
milimetro = v1 * 1000

print('Valor em metros: {}\n Valor em centimetros: {:.0f}\n Valor em milimetros: {:.0f}'.format(v1, centimetro,milimetro))