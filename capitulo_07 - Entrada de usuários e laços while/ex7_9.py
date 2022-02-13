'''
7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um laço
while para remover todas as ocorrências de 'pastrami' e sandwich_orders.
Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches.
'''

sandwich_orders = ['pastrami', 'bmt italiano', 'carne supreme', 'pastrami',
                   'frango teriyaki', 'steak churrasco', 'pastrami']
finished_sandwiches = []

print('\n{:*^60}'.format(' LANCHONETE PYTHON '))
print("""\

** COMUNICADO IMPORTANTE **

Caros clientes,

Sinto em informá-los que no momento não estamos tendo o sanduíche de pastrami!

Sentimos muito pelo incoveniente.
""")

#Removendo o sanduíche pastrami da lista de pedidos feitos
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#Preparação dos sanduíches
print('\n{:*^60}'.format(' PREPARAÇÃO DE SANDUÍCHES '))

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(
        f'\nEstamos preparando o seu sanduíche {current_sandwich.title()}...')

    finished_sandwiches.append(current_sandwich)

#Finalização dos sanduíches
print('\n{:*^60}'.format(' SANDUÍCHES FINALIZADOS '))

for sandwich in finished_sandwiches:
    print(f'\nSeu sanduíche {sandwich.title()} já está pronto!')

print('\nTodos sanduíches preparados!')