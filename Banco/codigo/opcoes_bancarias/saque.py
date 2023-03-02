#saque

import os

def saque(id_usuario):

    while True:

        try: 

            os.system("cls")

            valor_saque=float(input("Digite um valor pra sacar:"))

            break

        except:

            continue

    dinheiro_usuario=open(f"usuarios\\{id_usuario}\\dinheiro.txt", "r")

    dinheiro_limpo=dinheiro_usuario.readlines()

    dinheiro_usuario.close()

    dinheiro_limpo=float(dinheiro_limpo[0])

    if valor_saque <= dinheiro_limpo:

        dinheiro_limpo-=valor_saque

        dinheiro_sacado=open("sacado.txt","w")

        dinheiro_sacado.write(f"R$ {valor_saque}")

        dinheiro_sacado.close()

        dinheiro_usuario=open(f"usuarios\\{id_usuario}\\dinheiro.txt", "w")  

        dinheiro_usuario.write(f"{dinheiro_limpo}") 

        dinheiro_usuario.close()

        os.system("cls")

        print(f"R$ {valor_saque} sacado com sucesso.")
    
    else:

        os.system("cls")

        print(f"Nao foi possivel sacar R$ {valor_saque}.")
    
    os.system("pause")