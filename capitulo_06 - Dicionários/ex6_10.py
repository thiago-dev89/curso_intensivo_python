'''
6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
apresente o nome de cada pessoa, juntamente com seus números favoritos

'''
favorite_numbers = {}
exit = True

while exit:
    print('\n{:*^60}'.format('Enquete de números favoritos'))
    person = input('\nInforme o seu nome: ')

    list_favorite_numbers = []

    print(f'\nOlá, {person.title()}. Agora informe os seus 3 primeiros números favoritos.')

    for i in range(3):
        favorite_number = int(input(f'\nInforme o seu {i + 1}º número favorito: '))
        list_favorite_numbers.append(favorite_number)
    
    favorite_numbers.update({person:list_favorite_numbers})

    repeat = input('\nAlguma outra pessoa para responder a enquete? ([S]im / [N]ão) : ')

    if repeat == 'N'.lower():

        for person in favorite_numbers.keys():
            print(f'\n{person.title()}, obrigado por responder a nossa enquete!')
            exit = False

print('\n{:*^60}'.format(" Resultado da enquete "))
for people, numbers in favorite_numbers.items():
    print(f'\n{people.title()} tem os segintes números favoritos: ')

    for number in numbers:
        print(f'- {number}')
