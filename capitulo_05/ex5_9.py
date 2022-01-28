'''
5.9 – Sem usuários

Acrescente um teste if em hello_admin.py para garantir
que a lista de usuários não esteja vazia.

• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
usuários!

• Remova todos os nomes de usuário de sua lista e certifique-se de que a
mensagem correta seja exibida.

'''
#Teste com lista de usuários preenchidas
users = ['thiago', 'pedro', 'admin', 'eric', 'linus', 'luiz']

#Teste com a lista de usuários vazias.
#users = []

if users:
    for user in users:
        if user == 'admin':
            print(f'Olá {user}, gostaria de ver um relatório de status?')
        else:
            print(f'Olá {user.title()}, obrigado por fazer login novamente.')
else:
    print('Precisamos encontrar alguns usuários!')
    