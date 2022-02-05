'''
7.1 – Locação de automóveis: Escreva um programa que pergunte ao usuário qual
tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse carro, por
exemplo, “Deixe-me ver se consigo um Subaru para você.”
'''

print('{:-^60}'.format(' Sistema de aluguel de carros '))

print('\nSeja bem-vindo ao nosso sistema de aluguel de carros.\n')

nome = input('Qual o seu nome? ')

print(f'\nOk, {nome}. Agora preciso saber qual o tipo de carro que gostaria de alugar.')
tipo_carro = input('\nInforme o tipo de carro: ')

print(f'\nDeixe-me ver se consigo um {tipo_carro} para você.') 