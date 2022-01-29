'''
6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.
'''

rios = {
    'nilo' : 'egito',
    'amazonas' : 'brasil',
    'yangtze' : 'china',
    'mississipi' : 'estados unidos',
    'ganges' : 'índia',
    'lena' : 'rússia',
    'fraser' : 'canadá',
}

#Exibe os nomes dos rios incluídos no dicionário
print('\n{:*^60}'.format(' Nome dos rios inclusos na base '))
for rio in sorted(rios.keys()):
    print(f'- {rio.title()}')

#Exibe os nomes dos países incluídos no dicionário
print('\n{:*^60}'.format(' Nome dos países inclusos na base '))
for pais in rios.values():
    print(f'- {pais.title()}')

print('\n{:*^60}'.format(' Rios pelo mundo '))
for rio, pais in rios.items():
    if pais.endswith('a'):
        print(f'\nO rio {rio.title()} corre pela {pais.title()}.')
    else:
        print(f'\nO rio {rio.title()} corre pelo {pais.title()}.')




