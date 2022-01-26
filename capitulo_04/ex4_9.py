'''
4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.
'''

lista_cubos = [cubos**3 for cubos in range(1, 11)]

for i in range(len(lista_cubos)):
    print(f'{i+1}³ = {lista_cubos[i]}')

