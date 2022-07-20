from getpass import getpass
from simple_chalk import chalk
import pandas as pd

five_stars = chalk.blue('*****')
titulo = chalk.yellow(' Sistema de Login com Python ')
stars = chalk.blue('***************************************')
#Início do Programa
print(stars)
print(f'{five_stars}{titulo}{five_stars}')
print(stars)

#Verifica se o usuário já tem cadastro
usuario_cadastrado = input(chalk.yellow('Você já possui cadastro? [S/N]:'))
#Transforma a resposta em uppercase
usuario_mauisculo = usuario_cadastrado.upper()

#Caso usuário tenha cadastro, o leva para tela de login
if usuario_mauisculo == 'S':
    print(stars)
    print('     Tela de Login     ')
    print(stars)
    planilha = pd.read_excel('users.ods')
    users = planilha.loc[..., 'users']
    for user in users:
        data = user
    print(user[0])
    user = input('Digite seu usuário:')
    password = getpass('Digite sua senha:')

#Caso não possua cadastro pergunta se o mesmo deseja efetuar um
elif usuario_mauisculo == 'N':
    cadastrar_usuario = input('Deseja cadastrar um novo usuário? [S/N]:').upper()
    if cadastrar_usuario != 'S':
        print(chalk.yellow('Tudo bem, tenha um bom dia!'))
    else:
        cadastro_efetuado = False
        print(chalk.blue('***************************************'))
        print(f'{five_stars} ------Tela de cadastro----- {five_stars}')
        print(chalk.blue('***************************************'))
        usuario = input(chalk.yellow('Escolha um nome de usuário:'))
        while cadastro_efetuado != True:
            senha = getpass('Escolha uma senha:')
            confirm_senha = getpass('Confirme sua senha:')
            if(confirm_senha != senha):
                print(chalk.red('As senhas digitadas são diferentes, tente novamente!'))
            else:
                print(chalk.green('Usuário cadastrado com Sucesso!'))
                cadastro_efetuado = True
else:
    print(chalk.red('Digite [S] para SIM, ou [N] para Não!'))