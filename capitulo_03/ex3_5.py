'''
    3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
          convidados não poderá comparecer ao jantar, portanto será necessário enviar
          um novo conjunto de convites. Você deverá pensar em outra pessoa para
          convidar.

          • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
            no final de seu programa, especificando o nome do convidado que não
            poderá comparecer.

          • Modifique sua lista, substituindo o nome do convidado que não poderá
            comparecer pelo nome da nova pessoa que você está convidando.

          • Exiba um segundo conjunto de mensagens com o convite, uma para cada
            pessoa que continua presente em sua lista.
'''

convidados = ['thiago', 'bernardo', 'tônia']

print(f'{convidados[0].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[1].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[2].title()}, você está convidado para o nosso jantar.')

print(f'\nInfelizmente, o convidado(a) {convidados[2].title()} não poderá comparecer ao jantar.')

# O convidado(a) Tônia não poderá comparecer ao jantar. Vamos convidar o Pedro
del (convidados[2])
convidados.insert(2, 'pedro souza')

print(f'O convidado(a) {convidados[2].title()} foi adicionado à lista de convidados.')

#Exibindo a lista de convidados novamente.
print(f'\n{convidados[0].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[1].title()}, você está convidado para o nosso jantar.')
print(f'{convidados[2].title()}, você está convidado para o nosso jantar.')
