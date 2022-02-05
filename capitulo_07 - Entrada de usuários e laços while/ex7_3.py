'''
7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.
'''

num = int(input('Informe um número: '))

if num % 10 == 0:
    print(f'O número {num} é múltiplo de 10.')
else:
    print(f'O número {num} não é múltiplo de 10.')
