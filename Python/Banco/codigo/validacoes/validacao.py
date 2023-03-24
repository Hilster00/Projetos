#validacao

import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl

def validacao(id):

    while True:
        id_loguin=""
        
        while id_loguin == "":
            os.system("cls")
            id_loguin=erro_ctrl("Informe o seu loguin:")
            id_loguin=id_loguin.upper()

        if id != id_loguin:  
            id_loguin="invalido"
        break
        
    if id_loguin != "invalido":
        importar_senha=open(f"usuarios\\{id_loguin}\\senha.txt","r")
        senha=importar_senha.readlines()
        importar_senha.close()
        senha=senha[0]
        os.system("cls")

        for tentativas in range (1,4):
            print(f"Tentativa {tentativas}")
            senha_loguin=erro_ctrl("Digite a senha de acesso:")
            
            if senha_loguin == senha:
                break
            
        if senha_loguin == senha:
            autenticacao=True

        else:
            print("Falha no loguin")
            autenticacao=False
        
        os.system("pause")
    
    else:
        autenticacao=False

    return autenticacao
