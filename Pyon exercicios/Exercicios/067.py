'''Faça um program que leia a tubuada de varios numeros
um de cada vez
pra cada valor digitado pelo usuario
o programa sera interrompido se o valor digitado for negativo'''
while True:
    print('=-=' * 5)
    valor = int(input('Digite o valor da tabuada: '))
    print('=-=' * 5)
    if valor < 0:
        break
    for x in range(1, 11):
        print(f'{valor} x {x} = {valor * x}')
print('Tabuada encerrada!')

