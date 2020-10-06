#faça um programa que leia a velocidade do carro se for acima de 80km/h mostre uma msg dizendo que foi multado
#a cada km acima da velocidade curta 7 R$ por cada km excedido

velocidade = int(input('Digite a velocidade do carro km/h: '))
multa = (velocidade - 80) *7

if velocidade > 80:
    print('Voce estava a {}km/h em uma pista de 80km/h, por isso foi multado em: {}R$.'.format(velocidade,multa))
else:
    print('A pista era de 80km/h e vc estava a {}km/h, parabens voce é um motorista consciente!'.format(velocidade))