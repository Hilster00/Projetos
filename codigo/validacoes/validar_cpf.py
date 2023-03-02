#validar cpf

import os

def validar_cpf():

    mensagem=""

    while True:

        os.system("cls")

        try:

            print(mensagem)

            cpf=input("Digite o seu cpf:")

            

            os.system("pause")

            if len(cpf) < 11:

                print(len(cpf))

                os.system("pause")

                continue

            cpf_valido=int(cpf)         

            break

        except:

            mensagem = "Cpf invalido"
    print(cpf)
    
    cpf=f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

    os.system("cls")
    
    return cpf