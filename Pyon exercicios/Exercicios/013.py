#peça salario e de o salario com 15% de aumento

salario = float(input('Qual o valor do seu salario? '))

aumento = (salario * 15/100) + salario

print('Seu salario é: R${:.2f} e com 15% de aumento vai ficar com: R${:.2f}, parabens!'.format(salario,aumento))