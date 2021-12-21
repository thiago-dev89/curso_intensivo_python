'''
3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.

• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas
pessoas para o jantar.

• Utilize pop() para remover os convidados de sua lista, um de cada vez, até
que apenas dois nomes permaneçam em sua lista. Sempre que remover um
nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
saiba que você sente muito por não poder convidá-la para o jantar.

• Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.

• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
uma lista vazia no final de seu programa.

'''
convidados = ['thiago souza', 'bernardo ferreira', 'tônia silva']

print('\n{:*^60}'.format(' Lista atual de convidados '))
print(f'{convidados[0].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[1].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[2].title()}, você está convidado para o nosso jantar.')

print('\nPessoal, encontrei uma mesa de jantar maior. Poderemos convidar mais pessoas!!')

convidados.insert(0, 'pedro souza')
convidados.insert(1, 'paulo silva')
convidados.append('regina souza')

print('\n{:*^60}'.format(' Nova lista de convidados '))
print(f'{convidados[0].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[1].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[2].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[3].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[4].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[5].title()}, você está convidado para o nosso jantar.\n')

# Ah não, a mesa não chegará a tempo!
print('\nDesculpem, mas posso convidar apenas duas pessoas para o jantar.')

#Excluindo as pessoas da lista de convidados
print('\n{:*^60}'.format(' Excluindo convidados da lista '))

nome = convidados.pop()
print(f'\nDesculpe, {nome.title()}. Não temos vagas na mesa.')

nome = convidados.pop()
print(f'Desculpe, {nome.title()}. Não temos vagas na mesa.')

nome = convidados.pop()
print(f'Desculpe, {nome.title()}. Não temos vagas na mesa.')

nome = convidados.pop()
print(f'Desculpe, {nome.title()}. Não temos vagas na mesa.')

'''
Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.
'''
print('\n{:*^60}'.format(' Nova lista de convidados '))
print(f'{convidados[0].title()}, você está convidado para o jantar!')
print(f'{convidados[1].title()}, você está convidado para o jantar!')

'''
Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
uma lista vazia no final de seu programa.
'''
del (convidados[0])
del (convidados[0])

print()
print(convidados)


