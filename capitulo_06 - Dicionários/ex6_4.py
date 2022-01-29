'''
6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com
um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua
sequência de instruções print por um laço que percorra as chaves e os valores
do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
essas palavras e significados novos deverão ser automaticamente incluídos na
saída.
'''

glossario = {
    'string' : 'Uma cadeia de caracteres.',
    'comentario' : 'Uma nota em um programa que o interpretador Python ignora.',
    'lista' : 'Uma coleção de itens em uma ordem particular.',
    'loop' : 'Trabalho com uma coleção de itens, um de cada vez.',
    'dicionario' : 'Uma coleção de par contendo uma chave e um valor.',
    'chave' : 'O primeiro item do par chave/valor em um dicionário.',
    'valor' : 'Um item associado a uma chave em um dicionário.',
    'teste condicional' : 'A comparação entre dois valores.',
    'float' : 'Um valor numeral com componentes decimais.',
    'expressão booleana' : 'Uma expressão que é avaliada como True ou False.',
}

for palavra, definicao in glossario.items():
    print(f'\n{palavra.title()} : {definicao}')



