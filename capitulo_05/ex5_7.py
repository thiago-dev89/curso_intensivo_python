'''
5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então, escreva uma
série de instruções if independentes que verifiquem se determinadas frutas
estão em sua lista.

• Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.

• Escreva cinco instruções if. Cada instrução deve verificar se uma
determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma
frase, por exemplo, Você realmente gosta de bananas!

'''

favorite_fruits = []

while True:
    fruits = input("Digite sua fruta favorita - 's' para encerrar : ")

    if fruits == 'S' or fruits == 's':
        if not favorite_fruits:
            print('Você não informou nenhuma fruta!')
            break
        else:
            print('\nEssas são suas frutas favoritas')
            print(favorite_fruits)
            break
    favorite_fruits.append(fruits)
    print(f'Adicionando a fruta {fruits}...\n')
    
        

if 'banana' in favorite_fruits:
    print('\nVocê realmente gosta de bananas!')
if 'maçã' in favorite_fruits:
    print('Você realmente gosta de maçãs!\n')
if 'laranja' in favorite_fruits:
    print('Você realmente gosta de laranjas!\n')
if 'kiwi' in favorite_fruits:
    print('Você realmente gosta de kiwi!\n')
if 'melancia' in favorite_fruits:
    print('Você realmente gosta de melancias!\n')
