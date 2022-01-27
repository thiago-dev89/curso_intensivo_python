'''
4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.

Então faça o seguinte: 
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista.

Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize
um laço for para exibir a segunda lista. Certifique-se de que cada pizza
nova esteja armazenada na lista apropriada.
'''
my_pizzas = ['portuguesa', 'à moda', 'peperonni', 'margarita']
friend_pizzas = my_pizzas[:]

print('Minhas pizzas: ')
for pizza in my_pizzas:
    print(f'- {pizza.title()}')

print('\nPizzas do meu amigo: ')
for pizza in friend_pizzas:
    print(f'- {pizza.title()}')

my_pizzas.append('calabresa')
friend_pizzas.append('presunto')

print('\nMinhas pizzas favoritas: ')
for pizza in my_pizzas:
    print(f'- {pizza.title()}')

print('\nPizzas favoritas do meu amigo: ')
for pizza in friend_pizzas:
    print(f'- {pizza.title()}')



