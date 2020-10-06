'''Crie uma tupla com contagem de 0 a 20
peça um numero entre 0 e 20 e mostre na tela'''

num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'outo', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
escolha = 0
while True:
    escolha = int(input('Digite um numero de 0 a 20: '))
    if escolha < 0 or escolha > 20:
        print('Valor errado')
    else:
        break


print(f'Digitou {num[escolha]}')

