'''Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e
 qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


'''print('=-='*10)
print('666 para encerrar!')
print('=-='*10)
media = valor_media = maior = valor = 0
menor = 999
c = ''

while valor != 666:

    valor = int(input('Digite um valor: '))

    if valor < 666:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

        valor_media += valor
        media += 1
        c = str(input('Quer Continuar? [ S ] / [ N ]: ')).upper()
        valor_media += valor
        media += 1
        if c not in 'S':
            valor = 666


print('Vc digitou {} e a media dos valores digitados é {:.1f}'.format(media - 2, valor_media / media))
print('O maior numero digitado é {} e o menor é {}'.format(maior, menor))'''

resposta = "S"
soma = quantidade = media = maior = menor = 0
while resposta in 'S':
    numero = int(input('Digite um numero: '))
    soma += numero
    quantidade += 1
    if quantidade ==  1:
        maior  = menor =  numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [ S ] / [ N ] : ')).upper()[0]
media = soma / quantidade
print('Voce digitou {} numeros e a media foi de {}'.format(quantidade, media))
print('O maior numero é {} e o menor é {}'.format(maior, menor))
