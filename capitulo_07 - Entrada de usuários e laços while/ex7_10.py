'''
7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse
visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
apresente os resultados da enquete.

'''

prompt_pergunta = '\nPERGUNTA: Se pudesse visitar um lugar do mundo, para onde você iria? '
prompt_pergunta += '\nRESPOSTA: '

prompt_encerrar = '\nAlguém a mais para responder a pesquisa? '
prompt_encerrar += "\nConfirme com [s]im ou [n]ão: "

respostas = {}

contador_pessoas = 1

pesquisa_ativa = True

while pesquisa_ativa:

    print('\n{:*^60}'.format(' PESQUISA FÉRIAS DOS SONHOS '))

    # Seta a chave 'pessoa' que será usada no dicionário 'respostas'
    chave_pessoa = 'pessoa' + str(contador_pessoas)

    nome = input('\nQual o seu nome? ')

    print(
        f'\nSeja bem-vindo a nossa pesquisa, {nome.title()}. Favor responder a pergunta abaixo...')

    lugar_escolhido = input(prompt_pergunta)

    respostas.update(
        {chave_pessoa: dict(nome=nome, lugar_escolhido=lugar_escolhido)})

    print(f'\nObrigado por responder a nossa pesquisa, {nome.title()}.')

    continua_pesquisa = input(prompt_encerrar)

    if continua_pesquisa == 'N'.lower():
        pesquisa_ativa = False

    contador_pessoas += 1

print('\n{:*^60}'.format(' RESULTADO DA PESQUISA '))

for idx, pessoa in enumerate(respostas, 1):
    print(f'{idx}° pessoa: ')
    print(f'\tNome: {respostas[pessoa]["nome"].title()}')
    print(f'\tLugar escolhido: {respostas[pessoa]["lugar_escolhido"].title()}\n')