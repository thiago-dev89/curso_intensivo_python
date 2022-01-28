'''
6.1 – Pessoa
Use um dicionário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
age e city. Mostre cada informação armazenada em seu dicionário.

'''
person = {
    'first_name': 'Thiago',
    'last_name' : 'Souza',
    'age' : 32,
    'city' : 'Belo Horizonte'
}

print('\n{:*^60}'.format(' Dados pessoais '))

print('Primeiro nome: ' + person['first_name'])
print('Sobrenome: ' + person['last_name'])
print('Idade: ' + str(person['age']))
print('Cidade: ' + person['city'])

