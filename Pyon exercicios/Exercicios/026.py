#peça uma frase e diga quantas vezes a letra "a" aparece , em qual posição ela aparece a primra vez  e em qual posição a ultima vez

frase = input('Digite uma frase: ').lower().strip()


print('A letra "A" aparece: {} vezes\n primeira vez q aparece é na posição: {}'.format(frase.count('a'), frase.find('a')+ 1))
print('e a ultima vez apareceu na posição: {}'.format(frase.rfind('a')+1))
