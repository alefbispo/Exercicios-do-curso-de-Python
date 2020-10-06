# gerar aleatoriedade com 4 alunos

import random
a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))
r = random.choice([a1, a2, a3, a4])
print('O aluno que vai apagar o quadro é: {}'.format(r))



