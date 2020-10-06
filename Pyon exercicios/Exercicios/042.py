'''Refaça o desafio 35
acrescentando que trinangulo sera formado
Equilatero todos os lados iguais
Isosceles dois lados iguais
Escaleno todos os lados diferentes'''

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
triangulo = r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r1 + r2
equilatero = r1 == r2 and r1 == r3
isosceles = r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2
escaleno = r1 != r2 and r1 != r3

if triangulo and equilatero:
    print('Pode fazer triangulo e é um EQUILATERO!')
elif triangulo and isosceles:
    print('Pode fazer triangulo e é um ISOSCELES!')
elif triangulo and escaleno:
    print('Pode fazer triangulo e é um ESCALENO')
else:
    print('NAO FAZ TRIANGULO!!')

