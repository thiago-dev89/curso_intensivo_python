'''
5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
em uma cadeia if-elif-else.

• Se o alienígena for verde, mostre uma mensagem informando que o jogador
ganhou cinco pontos.

• Se o alienígena for amarelo, mostre uma mensagem informando que o
jogador ganhou dez pontos.

• Se o alienígena for vermelho, mostre uma mensagem informando que o
jogador ganhou quinze pontos.

• Escreva três versões desse programa, garantindo que cada mensagem seja
exibida para a cor apropriada do alienígena.

'''

print('''\
Cores do alienígena:
1 - Verde
2 - Amarelo
3 - Vermelho

''')

alien_color = int(input('Escolha a sua opção de cor: '))

if alien_color == 1:
    print('\nCor escolhida foi a Verde.')
    print('Você ganhou 5 pontos!!')
elif alien_color == 2:
    print('\nCor escolhida foi a Amarelo.')
    print('Você ganhou 10 pontos!!')
elif alien_color == 3:
    print('\nCor escolhida foi a Vermelho.')
    print('Você ganhou 15 pontos!!')
else:
    print('\nOpção de cor inválida!')

