'''Crie um programa que leia idade e sexo de varias pessoas
e pergunte se o usuario quer conrinuar
no final mostre
quantas pessoas tem mais de 18 anos
quantos homens foram cadastrados
e quantas mulheres tem menos de 20 anos'''

pessoas_18 = mulher_20 = homen = 0

while True:
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Escolha um sexo\n'
                     '[ M ] / [ F ] : ')).strip().upper()[0]
    continuar = str(input('Quer continuar cadastrando?\n'
                          '[ S ] / [ N ] : ')).upper().strip()[0]
    if continuar in 'N':
        break
    if idade > 18:
        pessoas_18 += 1
    if sexo in 'M':
        homen += 1
    if sexo in 'F' and idade < 20:
        mulher_20 +=1

print(f'{pessoas_18} tem mais de 18 anos')
print(f'{homen} homens foram cadastrados')
print(f'{mulher_20} Mulher tem menos de 18 anos')
