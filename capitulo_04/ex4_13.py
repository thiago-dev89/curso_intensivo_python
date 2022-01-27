'''
4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos
de comida. Pense em cinco pratos simples e armazene-os em uma tupla.

• Use um laço for para exibir cada prato oferecido pelo restaurante.

• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.

• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em
seguida, use um laço for para exibir cada um dos itens do cardápio
revisado.

'''
itens_cardapio = (
    'café filtrado', 'macchiato', 'expresso com chantilly', 'café americano'
)

print('{:*^60}'.format('Itens do cardápio'))
for item in itens_cardapio:
    print(f'- {item.title()}')

itens_cardapio = (
    'café filtrado', 'macchiato', 'mocha branco', 'caramelo macchiato', 'flat white'
)

print('\n{:*^60}'.format('Novos itens do cardápio'))
for item in itens_cardapio:
    print(f'- {item.title()}')


