"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção
  (sem usar o sort()). No final,
   mostre a lista ordenada na tela."""
lista = []

for x in range(0, 5):
    resposta = int(input(f'Digite o {x+1}º valor: '))
    if x == 0 or resposta > lista[-1]:
        lista.append(resposta)
        print('Adidionado no final da lista')
    else:
        posisao = 0
        while posisao < len(lista):
            if resposta < lista[posisao]:
                lista.insert(posisao, resposta)
                print(f'Adicionado na posição {posisao} da lista')
                break
            posisao += 1

print(lista)



