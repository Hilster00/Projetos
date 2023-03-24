#criar id
#2oucyqcc8

import os
import random

lista_caracteres=("1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

def criar_id():
    
    id_usuario="" 

    for vezes in range (0, 10):

        item=random.choice(lista_caracteres)

        id_usuario=f"{id_usuario}{item}"

    return id_usuario
