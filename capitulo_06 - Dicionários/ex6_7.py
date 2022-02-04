'''
6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
(página 147). Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista de
pessoas com um laço. À medida que percorrer a lista, apresente tudo que você
sabe sobre cada pessoa.
'''
people = []

person = {
    'first_name' :'Albert',
    'last_name' : 'Einsten',
    'age' : 143,
    'city' : 'Ulm',
}

people.append(person)

person = {
    'first_name' :'Isaac',
    'last_name' : 'Newton',
    'age' : 379,
    'city' : 'Woolsthorpe-by-Colsterworth',
}

people.append(person)

person = {
    'first_name' :'Stephen',
    'last_name' : 'Hawking',
    'age' : 80,
    'city' : 'Oxfordshire',
}

people.append(person)

for person in people:
    name = person['first_name'] + ' ' + person['last_name']
    age = person['age']
    city = person['city']

    print(f'\n{name}, de {city}, tem {age} anos de idade!')
