#mudar_idade

import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl

def mudar_idade(id):

    idade=open(f"usuarios\\{id}\\nome.txt","r")

    idade_limpa=idade.readlines()

    nome=idade_limpa[0]

    idade_limpa=idade_limpa[1]

    idade.close()

    while True:

        try:
            os.system("cls")

            nova_idade=erro_ctrl("Digite a nova idade:")

            nova_idade=int(nova_idade)

            break

        except:

            print("Idade invalida")

            os.system("pause")        
    
    if nova_idade > int(idade_limpa):

        idade=open(f"usuarios\\{id}\\nome.txt","w")

        idade.write(f"{nome}{nova_idade}")

        idade.close()

        os.system("cls")

        print(f"Idade {nova_idade} salva com sucesso.")

        os.system("pause")
    
    else:

        os.system("cls")

        print("Nova idade não pode ser menor do que a antiga")

        os.system("pause")