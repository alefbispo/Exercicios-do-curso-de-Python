''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
frase = input('Digite uma frase: ').strip().upper().split()
junto = ''.join(frase)
inverso = ''

for x in range(len(junto) -1, -1, -1):
    inverso += junto[x]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não é um palindromo!')
print(junto, inverso)