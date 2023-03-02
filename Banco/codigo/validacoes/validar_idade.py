#validar_idade

import os

def validar_idade():

    mensagem=""

    while True:

        os.system("cls")

        print(mensagem)

        try:

            idade=int(input("Digite a sua idade:"))

            break
        
        except:

            mensagem="Idade invalida"
    
    return idade