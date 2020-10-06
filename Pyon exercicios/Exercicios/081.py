"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
v = 0
lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resposta = str(input('Quer salvar mais valores: [s/n]: ')).lower()
    v += 1
    if resposta in 'n':
        print('saindo do loop..')
        break
print(f'Foram digitados {v} numeros')
lista.sort(reverse=True)
print(f'A lista em forma decrescente fica: {lista}')
if 5 in lista:
    print('Valor 5 esta na lista')
else:
    print('Valor 5 nao esta na lista')
