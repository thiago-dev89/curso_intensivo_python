'''
6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o
tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer 
isso, apresente tudo que você sabe sobre cada animal de estimação.

'''
pets = []

pet = {
    'tipo' : 'serpente',
    'nome' : 'cruella',
    'dono' : 'eric',
    'peso' : 32,
    'comida' : 'mamíferos pequenos',
}

pets.append(pet)

pet = {
    'tipo' : 'gato',
    'nome' : 'tom',
    'dono' : 'bernardo',
    'peso' : 5,
    'comida' : 'ração',
}

pets.append(pet)

pet = {
    'tipo' : 'cachorro',
    'nome' : 'ted',
    'dono' : 'steven',
    'peso' : 8,
    'comida' : 'ração',
}

pets.append(pet)

for pet in pets:
    print(f"\nInformações sobre o pet {pet['nome'].title()}: ")

    for k, v in pet.items():
        print(f"\t - {k.title()}: {v}")
