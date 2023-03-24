#tela_configuracoes_usuario

import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl

def configuracoes_usuario():

    mensagem=""
    opcoes=["1","2","3"]

    while True:
        os.system("cls")
        print(mensagem)
        
        print("(1) Alterar informações pessoais")
        print("\n")
        print("(2) Encerrar conta")
        print("\n")
        print("(3) Voltar")
        print("\n")

        opcao=erro_ctrl("Digite a opção desejada:")

        if opcao not in opcoes:
            mensagem ="\nOpcao invalida\n"
            continue

        break
        
    return opcao
