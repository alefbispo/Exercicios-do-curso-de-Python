'''Desenvolva uma logica que leia o peso e a altura de uma pessoa
calcule seu IMC e mostre
< 18.5 abaixo do peso
entre 18.5 e 25 peso ideal
25 ate 30 acima do peso
acima de 40 obesidade morbida'''

peso =  float(input('Digite seu peso: '))
altura =  float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 > imc < 25:
    print('Peso ideal!')
elif 25 > imc < 30:
    print('Acima do peso!')
elif 30 > imc < 40:
    print('Obesidade!')
elif imc > 40:
    print('Obesidade Morbida!')
