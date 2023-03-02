#validacao transfereencia

import os

def validar_transferencia(id_usuario, valor_transferencia):

    dinheiro_usuario=open(f"usuarios\\{id_usuario}\\dinheiro.txt","r")

    dinheiro_limpo=dinheiro_usuario.readlines()

    dinheiro_usuario.close()

    dinheiro_limpo=float(dinheiro_limpo[0])

    if not (dinheiro_limpo < valor_transferencia):

        valido=True
    else:

        valido=False
        
    return valido