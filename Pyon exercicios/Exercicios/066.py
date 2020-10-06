'''Crie um programa que leia varios numeros inteiros
o programa so vai parar qunado o usuario digitar 999
no final mostre a soma entre eles e quanto foram digitados'''
soma = total = 0

while True:
    valor = int(input('## 999 para parar ###\n'
                      'Digite um valor: '))

    if valor == 999:
        break
    total += 1
    soma += valor
print(f'Vc digitou {total} valores e a soma entre eles é {soma}')