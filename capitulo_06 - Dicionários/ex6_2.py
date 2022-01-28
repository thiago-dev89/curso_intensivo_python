'''
6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos
de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
dicionário. Pense em um número favorito para cada pessoa e armazene cada
um como um valor em seu dicionário. Exiba o nome de cada pessoa e seu
número favorito. Para que seja mais divertido ainda, faça uma enquete com
alguns amigos e obtenha alguns dados reais para o seu programa.

'''
favorite_numbers = {
    'thiago' : 7,
    'luis' : 20,
    'marcos' : 150,
    'peter' : 24,
    'eric' : 100000,
    'marlon' : 69,
}

number = favorite_numbers['thiago']
print(f'O número favorito do Thiago é : {number}.')

number = favorite_numbers['luis']
print(f'\nO número favorito do Luis é : {number}.')

number = favorite_numbers['marcos']
print(f'\nO número favorito do Marcos é : {number}.')

number = favorite_numbers['peter']
print(f'\nO número favorito do Peter é : {number}.')

number = favorite_numbers['eric']
print(f'\nO número favorito do Eric é : {number}.')

number = favorite_numbers['marlon']
print(f'\nO número favorito do Marlon é : {number}.')