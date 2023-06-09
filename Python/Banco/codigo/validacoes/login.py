#login

import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl

def login():
    os.system("cls")    
    id_login=""

    while True:        
        id_login=erro_ctrl("Informe o seu login:")
        id_login=id_login.upper()
        os.system("cls")

        if os.path.exists(f"usuarios\{id_login}") == False:  
            os.system("cls")
            print(f"Loguin {id_login} invalido")
            continue
            
        break
    
    importar_senha=open(f"usuarios\{id_login}\senha.txt","r")
    senha=importar_senha.readlines()
    importar_senha.close()

    senha=senha[0]
    os.system("cls")

    for tentativas in range (1,4):
        print(f"Tentativa {tentativas}")
        senha_login=input("Digite a senha de acesso:")
        
        if senha_login == senha:
            break

    if senha_login == senha:
        print("Loguin realiado com sucesso")
        login=True

    else:
        print("Falha no login")
        login=False
    
    os.system("pause")
    return [login, id_login]
