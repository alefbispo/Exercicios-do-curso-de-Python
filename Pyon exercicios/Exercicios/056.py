'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo
qual é o nome do homem mais velho
quantas mulheres têm menos de 20 anos.'''
media = 0
nome_velho = ''
idade_velho = 0
idade_mulher = 0
soma_idade = 0
for x in range(1, 5):
    print('------{}º NOME ------'.format(x))
    nome = str(input('Digite o nome: ')).upper()
    idade = int(input('A idade: '))
    sexo = str(input('Sexo [M/F]:')).upper()
    soma_idade += idade
    if x == 1 and sexo == 'M':
        nome_velho = nome
        idade_velho = idade
    if sexo == 'M' and idade > idade_velho:
            idade_velho = idade
            nome_velho = nome
    if sexo == 'F' and idade < 20:
        idade_mulher += 1

media += soma_idade
print('A media das idades é de: ', media / 4)
print('O homen mais velho se chama {} e tem {} anos!'.format(nome_velho, idade_velho))
if idade_mulher == 1:
    print('Apenas uma mulher tem menos que vinte anos!')
else:
    print('{} mulheres tem menos de 20 anos!'.format(idade_mulher))




