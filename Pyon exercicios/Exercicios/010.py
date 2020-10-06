#quantos dolares da pra comprar com o valor inserido (dolar valendo 3.27)

v = float(input('quanto vc tem na carteira? R$'))

d = v / 3.27

print('Com esse valor vc pode comprar: R${:.2f}'.format(d))
