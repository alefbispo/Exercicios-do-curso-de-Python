""" Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
 Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""


expressao = list(str(input('Digite uma expressão aritimetica:  ')))


if expressao.count("(") != expressao.count(")"):
    print('errado')

else:
    print('Certo')
print(expressao)
