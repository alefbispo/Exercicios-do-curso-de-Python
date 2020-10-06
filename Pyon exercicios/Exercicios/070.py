'''Crie um programa que leia varios produtos
pergunte se quer continuar
o total de gasto na compra
quantos produtos custam mais que 1000
o nome do produto mais barato'''

contador =total = quant = preco_b =0
nome_b = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$ '))
    continuar = str(input('Quer continuar?\n'
                          '[ S ] / [ N ] ')).strip().upper()[0]
    total += preco
    contador += 1

    if preco > 1000:
        quant += 1

    if contador == 1:
        nome_b = nome
        preco_b = preco

    if preco < preco_b:
        nome_b = nome
        preco_b = preco

    if continuar in 'N':
        break


print(f'O total gasto na compra foi R${total:.2f}')
print(f'{quant} produtos tem valor superior a R$ 1000')
print(f'O produto mais barato chama {nome_b} e custa R${preco_b:.2f}')