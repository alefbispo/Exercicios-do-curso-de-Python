#pedir a altura e a largura de uma parede e dizer quantos litros de tinta vai gastar sabendo que cada litro de tinta pinta 2m2

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
tinta = (altura * largura) / 2

print('Voce tem a area de {}x{} e sua parede tem a area de: {}M² \n voce vai precisar de {:.2f} litros de tinta pra pintar a parede!!'.format(altura, largura, area, tinta))


