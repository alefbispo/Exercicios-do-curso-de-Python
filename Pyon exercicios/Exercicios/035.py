#peça 3 retas e diga se forma um triangulo

reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas PODEM formar um triangulo!!!')
else:
    print('As retas  NÃO formam um  triangulo...')
