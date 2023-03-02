#tela_opcoes_bancarias

import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl


def tela_opcoes_bancarias():

    mensagem=""

    while True:

        os.system("cls")

        print(mensagem)

        print("(1) Saque")

        print("\n")

        print("(2) Deposito")

        print("\n")

        print("(3) Transferencia")

        print("\n")

        print("(4) Extrato Bancario")

        print("\n")

        print("(5) Voltar")

        print("\n")

        opcao=erro_ctrl("Digite a opcao desejada:")

        opcoes=("1","2","3","4","5")

        if opcao not in opcoes:

            mensagem=f'Opcao "{opcao}" invalida'

        else:

            break
    
    return opcao