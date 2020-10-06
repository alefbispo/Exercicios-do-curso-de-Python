#pedir dias de alugel do carro e km rodado com ele, cada dia vale R$60 e cada km rodado vale R$0.15

dias = int(input("Quantos tidas voce ficou com o carro?: "))
km = float(input('Quantos km vc rodou com ele? '))
divida = (dias * 60) +  (km * 0.15)

print('Dias alugados: {} \nKM rodado: {} \ntotal a pagar R$: {:.2f}'.format(dias,km,divida))