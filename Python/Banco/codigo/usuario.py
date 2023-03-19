#usuario

import os
from codigo.telas.tela_usuario_logado import tela_usuario_logado
from codigo.opcoes_bancarias.opcoes_bancarias_usuario import opcoes_bancarias
from codigo.configuracoes.configuracoes_bancarias_usuario import configuracoes_bancarias_usuario

def usuario(id):

    while True:
    
        opcao=tela_usuario_logado()

        if opcao == "1":

            opcoes_bancarias(id)
            

        elif  opcao== "2":

            configuracoes_bancarias_usuario(id)
            
        else:

            exit()
