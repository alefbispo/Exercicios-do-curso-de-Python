'''crie uma tupla  com 20 priemiros times de futebol na ordem de qualificação
mostre os 5 primeiros colocados
os 4 ultimos
em ordem alfabetica
em q posição esta o chapecoence'''

times = ('Atletico', 'Internacional', 'São paulo', 'palmeiras', 'vasco', 'flamengo', 'fluminence', 'sporte recife', 'santos', 'fortaleza',
         'atletico pr', 'ceara sc', 'atletico go', 'gremio', 'corinthians', 'coritiba', 'bragantino', 'botafogo', 'goias', 'bahia')

print('')
print('A lista de times é: ', times)
print('*-*' * 20)
print('')
print('Os 5 primeiros colocados são: ',times[:5])
print('*-*' * 40)
print('')
print('Os quatro ultimos são: ', times[-4:])
print('*-*' * 40)
print('')
print('Os times em ordem alfabetica: ', sorted(times))
print('*-*' * 40)
print('')
print('A posição do Corinthians é: ', times.index('corinthians')+1)