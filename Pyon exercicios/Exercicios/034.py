#receba o vaor do funcionario
#se for maior q 1250 tera aumento de 10%
# se for menor aumento de 15%

salario = float(input('Digite o valor do salario: '))

if salario <= 1250.00:
    print('Seu salario é R$ {:.2f} e teve aumento de 15% agora é: R$ {:.2f}'.format(salario, (salario * 0.15) + salario))
else:
    print('Seu salario é R$ {:.2f} e com aumento de 10% agora é: R$ {:.2f}'.format(salario,(salario * 0.10) + salario))


