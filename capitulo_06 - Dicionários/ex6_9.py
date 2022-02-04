'''
6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
três nomes para usar como chaves do dicionário e armazene de um a três lugares
favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante,
peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o
dicionário com um laço e apresente o nome de cada pessoa e seus lugares
favoritos
'''

favorite_places = {}
exit = True

while exit:
    print('\n{:-^60}'.format(' Enquete de lugares favoritos '))

    person = input("Informe o seu nome : ")
    
    list_favorite_places = []
    
    print(f'\nOlá, {person.title()}. Agora informe os seus 3 lugares favoritos\n')
    
    for i in range(3):
        favorite_place = input(f'Informe o seu {i + 1}° lugar favorito: ')
        list_favorite_places.append(favorite_place)
            
    favorite_places.update({person:list_favorite_places})
    
    repeat = input("\nAlguma outra pessoa gostaria de responder? ([S]im ou [N]ão) : ")

    if repeat == 'N'.lower():

        for person in favorite_places.keys():
            print(f'\n{person.title()}, obrigado por responder a nossa enquente!')
        exit = False

print('\n{:-^60}'.format('Resultado da enquete'))
for person, place in favorite_places.items():
    print(f'\n{person.title()} tem os seguintes lugares favoritos: ')

    for places in place:
        print(f'- {places.title()}')
        
