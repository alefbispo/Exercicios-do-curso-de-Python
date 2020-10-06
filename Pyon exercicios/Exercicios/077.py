'''Leia uma tupla com palavras
e mostre suas vogais'''

lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',\
        'mercado', 'programador', 'futuro')


for p in lista:
    print(f'\n\033[mNa palavra \033[:31m{p.upper()}\033[m temos as vogais: \033[:31m', end='')
    for palavra in p:
        if palavra in 'aeiou':
            print(palavra.upper(), end=' ')



0