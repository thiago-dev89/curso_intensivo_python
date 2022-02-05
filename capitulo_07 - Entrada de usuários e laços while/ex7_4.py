'''
7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.
'''

prompt = '\nQual ingrediente você quer na pizza? '
prompt += "\nPara encerrar, digite 'sair': "

while True:
    ingrediente = input(prompt)

    if ingrediente != 'sair':
        print(f'\nIngrediente {ingrediente} será adicionado à sua pizza!')
    else:
        break