#transferir

import os

def transferir(id_usuario,valor,conta_destino):

    dinheiro_usuario=open(f"usuarios\\{id_usuario}\\dinheiro.txt", "r")

    dinheiro_limpo=dinheiro_usuario.readlines()

    dinheiro_usuario.close()

    dinheiro_limpo=float(dinheiro_limpo[0])    

    dinheiro_destino=open(f"usuarios\\{conta_destino}\\dinheiro.txt", "r")

    dinheiro_destino_limpo=dinheiro_destino.readlines()    

    dinheiro_destino.close()

    dinheiro_destino_limpo=float(dinheiro_destino_limpo[0])

    dinheiro_destino_limpo+=valor

    dinheiro_limpo-=valor

    dinheiro_usuario=open(f"usuarios\\{id_usuario}\\dinheiro.txt", "w")

    dinheiro_destino=open(f"usuarios\\{conta_destino}\\dinheiro.txt", "w") 

    dinheiro_destino.write(f"{dinheiro_destino_limpo}")

    dinheiro_usuario.write(f"{dinheiro_limpo}")

    dinheiro_usuario.close()

    dinheiro_destino.close()