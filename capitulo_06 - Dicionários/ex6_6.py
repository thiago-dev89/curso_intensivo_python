'''
6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem
favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem
respondido à enquete, mostre uma mensagem agradecendo-lhes por responder.
Se ainda não participaram da enquete, apresente uma mensagem convidando-as a responder.
'''
participantes_enquete = ['peter', 'luis', 'pedro', 'eric', 'steve', 'john', 'mark', 'susan']

resposta_participantes_enquete = {
    'peter' : 'java',
    'pedro' : 'python',
    'steve' : 'c',
    'john' : 'python',
}
for p in participantes_enquete:
    if p in resposta_participantes_enquete.keys():
        print(f'\n{p.title()}, obrigado por responder a enquete!')
        print(f'Vejo que sua linguagem favorita é {resposta_participantes_enquete[p].title()}')
    else:
        print(f'\n{p.title()}, você ainda não respondeu a nossa enquete. ' + 
        'Pode responder agora?')


