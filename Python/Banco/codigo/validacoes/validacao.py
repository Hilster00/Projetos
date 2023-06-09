#validacao

import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl

def validacao(id):

    while True:
        id_login=""
        
        while id_login == "":
            os.system("cls")
            id_login=erro_ctrl("Informe o seu login:")
            id_login=id_login.upper()

        if id != id_login:  
            id_login="invalido"
        break
        
    if id_login != "invalido":
        importar_senha=open(f"usuarios\{id_login}\senha.txt","r")
        senha=importar_senha.readlines()
        importar_senha.close()
        senha=senha[0]
        os.system("cls")

        for tentativas in range (1,4):
            print(f"Tentativa {tentativas}")
            senha_login=erro_ctrl("Digite a senha de acesso:")
            
            if senha_login == senha:
                break
            
        if senha_login == senha:
            autenticacao=True

        else:
            print("Falha no login")
            autenticacao=False
        
        os.system("pause")
    
    else:
        autenticacao=False

    return autenticacao
