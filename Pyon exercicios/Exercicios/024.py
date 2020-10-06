#crie um programa que peça o nome de uma cidade e diga se a começa com a palavra "santo"

nome = input('Digite o nome de uma cidade: ').strip()
non = nome.lower()

print('O nome da sidade começa com "Santo"? true pra Sim e false pra Não!!\n',  ('santo' in non[:5]))
