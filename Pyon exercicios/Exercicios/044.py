'''Elavobe um programa que calcule o valor a ser prago por um produto
considerando o seu preço normal
e condição de pagamento
a vista/cheque 10% de desconto
a vista no cartao 5% de desconto
em ate 2x o preço normal
3x ou mais 20% de juros'''

print('==' * 20)
print('** Lojinha nota 10 **')
print('==' * 20)
valor = float(input('Qual o valor do produto? R$'))
print('''Para pagamento em Dinheiro ou Cheque digite: 1   
Para pagamento a vista no cartao digite:     2
Para parcelar em ate 2x no cartao digite:    3
Para carcelar em 3 ou mais vezes digite:     4''')
pagamento = int(input('Digite: '))

if pagamento == 1:
    print('Pagamento em dinheiro e cheque tem 10% de desconto o produto no valor de R${:.2f} vai ficar a {:.2f}'.format(valor, (valor - (valor * 10/100))))
elif pagamento == 2:
    print('Pagamento a vista no cartao tem desconto de 5% o produto vai dicar de R${:.2f} por R${:.2f}'.format(valor, valor - (valor * 5/100)))
elif pagamento == 3:
    print('Em ate 2x no cartao o prego nao tem alteração!')
elif pagamento == 4:
    print('Pagando em mais de 3x no cartao o valor tem acrescimo de 20% fica de R${:.2f} por  R${:.2f}'.format(valor, valor + (valor * 20/100)))


