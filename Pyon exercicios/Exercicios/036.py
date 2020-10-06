''' escreva um programa que aprove o emprestimo bancario para a compra de uma casa
perguntar o valor da casa
o salario
e quantos anos vai pagar
calcule o valor da prestação mensal nao pode ser maior que 30% do salario se nao sera negado '''


valor = float(input('Digite o valor da casa R$: '))
salario = int(input('Qual o valor do seu salario? '))
tempo = float(input('Em quantos anos voce vai pagar? '))
prestacao = valor / (tempo * 12)
porsentagem = salario * 30/100
divida = valor / tempo

print('Pra pagar uma casa de R${:.2f} em {} anos\n A prestação sera de R${:.2f}'.format(valor, tempo, prestacao))
if prestacao <= porsentagem:
    print('Parabens! seu emprestimo for aprovado!!')

else:
    print('Infelizmente nao foi aprovado seu financiamento!')
