#tela_usuario_logado

import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl

def tela_usuario_logado():

    mensagem=""

    while True:

        os.system("cls")

        print(mensagem)

        print("(1) Operacoes bancarias")

        print("\n")

        print("(2) Configuracoes do Usuario")

        print("\n")

        print("(3) Sair")

        print("\n")

        opcao=erro_ctrl('Digite a opcao desejada:')

        if opcao != "1" and opcao != "2" and opcao != "3":

            mensagem=f'opcao "{opcao}" invalida\n'

        else:

            break
    
    return opcao