#tela_inicial

import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl

def tela_inicial():

    mensagem = ""

    while True:
        os.system("cls")
        print("SENHOR_H Banco, o banco mais confiavel e seguro")
        print(mensagem)

        print("(1) Loguin")
        print("\n")
        print("(2) Cadastro")
        print("\n")

        opcao=erro_ctrl("Digite a opcao desejada:")

        if opcao !="1" and opcao != "2":
            mensagem="Opcao invalida"

        else:
            break
    
    return opcao
