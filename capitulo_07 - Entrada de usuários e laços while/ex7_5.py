'''
7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso
custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares.
Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes
o preço do ingresso do cinema.
'''

print('{:*^60}'.format('Bilheteria'))

while True:

    idade = int(input("\nQual a sua idade? \nInforme '0' para encerrar: "))

    if idade != 0:
        if idade >= 1 and idade < 3:
            print('\nIngresso gratuito!')
        elif idade >= 3 and idade <= 12:
            print('\nSeu ingresso custará R$ 10,00.')
        elif idade > 12:
            print('\nO ingresso custará R$ 15,00.')
    else:
        break
