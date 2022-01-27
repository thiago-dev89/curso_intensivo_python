'''
4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte: 

• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para
  exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são: 
  Use uma fatia para exibir três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
  exibir os três últimos itens da lista.
'''

comidas = ['pizza', 'hamburguer', 'sorvete', 'macarrão', 'batata frita', 'bife de frango']

print('Lista de comidas: ')
print(comidas)

#Exibindo os 3 primeiros da lista
print('\nOs 3 primeiros itens da lista: ')
for comida in comidas[:3]:
    print(comida.title())

print()

#Exibindo 3 itens do meio da lista
print('Os 3 itens do meio da lista')
for comida in comidas[2:5]:
    print(comida.title())

print()

#Exibindo 3 últimos itens da lista
print('Os 3 últimos itens da lista: ')
for comida in comidas[-3:]:
    print(comida.title())

