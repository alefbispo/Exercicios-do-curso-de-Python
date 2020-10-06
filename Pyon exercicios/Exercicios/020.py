#pedir 4 nomes de alunos e exebir os 4 aleatoriamente em sequencia

from random import shuffle

a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('do segundo aluno: '))
a3 = str(input('Do terceiro: '))
a4 = str(input('Do ultimo aluno: '))
lista = [a1, a2, a3, a4]

shuffle(lista)

print('A sequencia de alunos é: ', lista)

