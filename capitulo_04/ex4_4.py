'''
4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um
laço for para exibir os números. (Se a saída estiver demorando demais,
interrompa pressionando CTRL-C ou feche a janela de saída.)

'''

lista_milhao = []

#Adicionando os números a lista_milhao com o list comprehension
lista_milhao = (num for num in range(1, 1000001))

#Exibindo a lista_milhao
for num in lista_milhao:
     print(num)

