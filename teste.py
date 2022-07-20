import pandas as pd
from getpass import getpass
from simple_chalk import chalk

planilha = pd.read_excel('users.ods')

user = input(chalk.yellow('Usuário:'))
password = int(getpass(chalk.yellow('Senha:')))

matching_creds = (len(planilha[(planilha.users == user) & (planilha.passwords == password)]) > 0)

if matching_creds:
    print(chalk.green('Sucesso!'))
else:
    print(chalk.red('\nUsuário não cadastrado!'))
    print(chalk.red('Contate o administrador do sistema'))
