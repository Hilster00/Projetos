#deposito

import os

def deposito(id_usuario):          

    dinheiro_usuario=open(f"usuarios\\{id_usuario}\\dinheiro.txt", "r")

    dinheiro_limpo=dinheiro_usuario.readlines()

    dinheiro_usuario.close()

    dinheiro_limpo=float(dinheiro_limpo[0])

    while True:

        try:

            os.system("cls")

            valor_deposito=float(input("Digite o valor do deposito:"))

            break

        except:

            continue
        
    dinheiro_usuario=open(f"usuarios\\{id_usuario}\\dinheiro.txt", "w")

    dinheiro_limpo+=valor_deposito

    dinheiro_usuario.write(f"{dinheiro_limpo}")

    dinheiro_usuario.close()

    os.system("cls")

    print(f"R$ {valor_deposito} depositado com suceso.")

    os.system("pause")