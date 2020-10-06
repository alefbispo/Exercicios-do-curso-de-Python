'''Crie um programa que leia uma tupla unica
com nomes e precos em seguida
depois mostre os valores de forma tabular'''

itens = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)

print('*'* 30)
print('          Lista     ')
print('*'* 30)

for x in range(0, len(itens), 2):
    print(f'Produto  {itens[x]:.<30}   Custa   R$: {itens[x+1]:>7.2f}')

