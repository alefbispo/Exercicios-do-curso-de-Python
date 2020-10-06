#faça um programa que peça a distancia de uma viagem em km e calcule
#R$ 0.50 pra viagens ate 200km
#e 0.45 pra viagente maiores

km = int(input('Digite a distancia da viagem em km: '))
km_menor = km * 0.5
km_maior = km * 0.45

if km <= 200:
    print('Sua viagem tem {}km entao vai custar: {:.2f}R$'.format(km, km_menor))
else:
    print('Sua viagem tem {}km e vai custar: {:.2f}R$'.format(km, km_maior))