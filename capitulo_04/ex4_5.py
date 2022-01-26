'''
4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida, use min()
e max() para garantir que sua lista realmente começa em um e termina em um
milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é
capaz de somar um milhão de números.
'''

lista_milhao = [num for num in range(1, 11)]

print(f'Lista começa em {min(lista_milhao)}.')
print(f'Lista termina em {max(lista_milhao)}.')
print(f'A soma da lista = {sum(lista_milhao)}.')
