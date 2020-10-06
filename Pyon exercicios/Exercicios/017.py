#calcular o cateto da hipotenusa

#jeito matematico
"""co = float(input('Medida do cateto oposto: '))
ca =  float(input('Medida do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa é: {:.2f}'.format(hi))"""


#jeito com biblioteca
from math import hypot
co = float(input('Medida do cateto oposto: '))
ca =  float(input('Medida do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa é: {:.2f}'.format(hi))

