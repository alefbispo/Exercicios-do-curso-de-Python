'''faça um programa que leia duas notas do aluno e diga se foi aprovado ou reprovado
se a nots for 5 reprovado
se a nota for entre 5 e 6.9 recuperação
se for 7 ou mais aprovado'''

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
resutado = (n1 + n2) / 2

if resutado >= 7.0:
    print('Sua media foi: {} Aprovado! PARABENS!!!'.format(resutado))
elif resutado <= 5.0:
    print('Sua media foi: {} Reprovado! precisa se esforçar muito mais!!'.format(resutado))
elif 5 <= resutado <= 6.9:
    print('Sua media foi: {} Esta de recuperação!!'.format(resutado))
