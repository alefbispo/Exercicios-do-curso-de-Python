import math

angulo = float(input('Informe o angulo: '))
seno = math.asin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.atan(math.radians(angulo))

print('O angulo é: {:.2f}\n o seno é: {:.2f}\n o cosseno é: {:.2f}\n e a tangente é: {:.2f}'.format(angulo, seno, cosseno, tangente))

