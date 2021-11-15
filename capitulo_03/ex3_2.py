'''
3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de simplesmente exibir
      o nome de cada pessoa, apresente uma mensagem a elas. O texto de cada mensagem deve ser o mesmo,
      porém cada mensagem deve estar personalizada com o nome da pessoa.
'''
nomes = ["Thiago", "Bernardo", "Tônia", "Paulo"]
print('*{:^40}*'.format('Listas de amigos'))
print(f'Seja bem-vindo ao mundo Python, {nomes[0].title()}.')
print(f'Seja bem-vindo ao mundo Python, {nomes[1].title()}.')
print(f'Seja bem-vindo ao mundo Python, {nomes[2].title()}.')
print(f'Seja bem-vindo ao mundo Python, {nomes[3].title()}.')
