'''
7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito,
exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
contrário, informe que sua mesa está pronta
'''

print('\n{:*^60}'.format(' Sistema de reserva de mesa '))
print('\nSeja bem-vindo ao nosso sistema de reservas de mesa.\n')

nome = input('Qual o seu nome? ')

print(f'\nOk, {nome}. Preciso saber o número de pessoas para o jantar.\n')

grupo_jantar = int(input('Informe o número de pessoas para o jantar: '))

if grupo_jantar > 8:
    print(f'\nSr(a). {nome}. Infelizmente no momento não temos mesa disponível.')
else:
    print(f'\nSr(a). {nome}. Sua mesa está pronta.')
