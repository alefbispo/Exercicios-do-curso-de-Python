'''Refaça o DESAFIO 51,
 lendo o primeiro termo e a razão de uma PA,
  mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

primeiro = int(input('Qual o termo? '))
progressao = int(input('Pular de quanto em quanto? '))
contador = 1
termo = primeiro



while contador <= 10:
    print('{}'.format(termo), end=' > ')
    termo += progressao
    contador += 1
print('fim')
