'''
3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.

• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.

• Utilize insert() para adicionar um novo convidado no início de sua lista.

• Utilize insert() para adicionar um novo convidado no meio de sua lista.

• Utilize append() para adicionar um novo convidado no final de sua lista.

• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.

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