'''Crie um programa que simule um caixa elegtronico
no inicio pergunte o valor a ser sacado
o programa era informar quantas cedular de cada valor serao entregues
valores
50, 20, 10 e 1'''
valor =  int(input('Qual valor vc quer sacar? '))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'O total de {total_cedula} cedulas  de R${cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('Operação finalizada, confirme seu troco!')