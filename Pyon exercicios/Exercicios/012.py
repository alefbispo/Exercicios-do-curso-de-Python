#pede o preço e mostra quanto fica com 5% de desconto

preco = float(input('Qual o preço do produto? R$'))

d = preco - (preco * 5/100)


print('Sem desconto o valor é de: R${:.2f} e com 5% de desconto fica: R${:.2f}'.format(preco, d))
