#loguin

import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl

def loguin():

    os.system("cls")    

    id_loguin=""

    while True:        

        id_loguin=erro_ctrl("Informe o seu loguin:")

        id_loguin=id_loguin.upper()

        os.system("cls")

        if os.path.exists(f"usuarios\\{id_loguin}") == False:  

            os.system("cls")

            print(f"Loguin {id_loguin} invalido")

            continue

        break
    
    importar_senha=open(f"usuarios\\{id_loguin}\\senha.txt","r")

    senha=importar_senha.readlines()
    
    importar_senha.close()


    senha=senha[0]

    os.system("cls")

    for tentativas in range (1,4):

        print(f"Tentativa {tentativas}")

        senha_loguin=input("Digite a senha de acesso:")
        
        if senha_loguin == senha:

            break

    if senha_loguin == senha:

        print("Loguin realiado com sucesso")

        loguin=True

    else:

        print("Falha no loguin")

        loguin=False
    
    os.system("pause")

    return [loguin, id_loguin]