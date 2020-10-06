'''Melhore o DESAFIO 61,
 perguntando para o usuário se ele quer mostrar mais alguns termos.
  O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input('Qual o termo? '))
progressao = int(input('Pular de quanto em quanto? '))
contador = 1
termo = primeiro
cont = 1
total = 0
mais = 10


while mais != 0:
    total += mais
    while contador <= total:
        print('{}'.format(termo), end=' > ')
        termo += progressao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos quer adicionar a mais? '))
print('A progressão finalizada com {} termos mostrados.'.format(total))
