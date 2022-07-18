from calendar import c
import openpyxl
from getpass import getpass
from simple_chalk import chalk

five_stars = chalk.blue('*****')
titulo = chalk.yellow(' Sistema de Login com Python ')
#Início do Programa
print(chalk.blue('***************************************'))
print(f'{five_stars}{titulo}{five_stars}')
print(chalk.blue('***************************************'))

#Verifica se o usuário já tem cadastro
usuario_cadastrado = input(chalk.yellow('Você já possui cadastro? [S/N]:'))
#Transforma a resposta em uppercase
usuario_mauisculo = usuario_cadastrado.upper()

#Caso usuário tenha cadastro, o leva para tela de login
if usuario_mauisculo == 'S':
    print('Show de Bola!')
#Caso não possua cadastro pergunta se o mesmo deseja efetuar um
elif usuario_mauisculo == 'N':
    cadastrar_usuario = input('Deseja cadastrar um novo usuário? [S/N]:').upper()
    if cadastrar_usuario != 'S':
        print(chalk.yellow('Tudo bem, tenha um bom dia!'))
    else:
        print(chalk.blue('***************************************'))
        print(f'{five_stars} ------Tela de cadastro----- {five_stars}')
        print(chalk.blue('***************************************'))
        usuario = input(chalk.yellow('Escolha um nome de usuário:'))
        def cadastra_senha():
            senha = getpass('Escolha uma senha:')
            confirm_senha = getpass('Confirme sua senha:')
            if confirm_senha == senha:
                print(chalk.green('Usuário cadastrado com Sucesso!'))
            else:
                while confirm_senha != senha:
                    print(chalk.red('As senhas digitadas são diferentes, tente novamente!'))
                    cadastra_senha()
        cadastra_senha()
else:
    print(chalk.red('Digite [S] para SIM, ou [N] para Não!'))