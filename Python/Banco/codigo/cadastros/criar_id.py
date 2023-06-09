#criar id
#2OUCYQCC8 ou #S085S2WB7Q

import os
import random

lista_caracteres=[chr(i) for i in range(ord("A"),ord("Z")+1)]
lista_caracteres.extend([str(i) for i in range(10)])

def criar_id(*,q=10):
    
    caracteres=random.choices(lista_caracteres,k=q)

    return "#"+"".join(caracteres)
    
if __name__ == "__main__":
    print(criar_id())
