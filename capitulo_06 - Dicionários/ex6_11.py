'''
6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações sobre
cada cidade e inclua o país em que a cidade está localizada, a população
aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade
devem ser algo como country, population e fact. Apresente o nome de cada
cidade e todas as informações que você armazenou sobre ela.

'''

cities = {
    'toquio': {
        'pais': 'japão',
        'populacao': 37435191
    },
    'delhi': {
        'pais': 'india',
        'populacao': 29399141
    },
    'xangai': {
        'pais': 'china',
        'populacao': 26317104
    },
    'sao paulo': {
        'pais': 'brasil',
        'populacao': 21846507
    },
    'cidade do mexico': {
        'pais': 'méxico',
        'populacao': 21671908
    }
}

print('{:-^60}'.format(' Lista das 5 cidades mais populosas do mundo '))

for city, city_info in cities.items():
    pais = city_info['pais']
    populacao = city_info['populacao']

    print(f'\n- {city.title()} : ')
    if pais.endswith('a'):
        print(f'   Está na {pais.title()} e tem {populacao} habitantes.')
    else:
        print(f'   Está no {pais.title()} e tem {populacao} habitantes.')
