#faca um programa que leia de 0 a 9999 e mostre na tela os numeros separados
# ex: 1834
# unidade 4 dezena 3 sentena 8 e milhar 1

num = (input('Digite um numero entre 0 e 9999: '))

#modo "string"
print(f'O numero é: {num}\n '
      f'unidade {num[3]}\n'
      f'dezena {num[2]}\n'
      f'sentena {num[1]}\n'
      f'milher {num[0]}')

#modo matematico "requer numero int"
# print(f'O numero é: {num}\n '
#      f'unidade {num // 1 % 10}\n'
#      f'dezena {num // 10 % 10}\n'
#      f'sentena {num // 100 % 10}\n'
#      f'milher {num // 1000 % 10}')
