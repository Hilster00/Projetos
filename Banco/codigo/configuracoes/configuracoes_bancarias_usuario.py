#configuracoes_bancarias_usuario

import os
from codigo.validacoes.validacao import validacao
from codigo.validacoes.importar_ctrl_c import erro_ctrl
from codigo.configuracoes.mudar_idade import mudar_idade
from codigo.configuracoes.mudar_senha import mudar_senha
from codigo.telas.tela_configuracoes_usuario import configuracoes_usuario
from codigo.telas.tela_alterar_informacoes import tela_alterar_informacoes

def configuracoes_bancarias_usuario(id):

    while True:

        opcao=configuracoes_usuario()

        if opcao=="1":

            while True:

                opcao=tela_alterar_informacoes()

                if opcao == "1":

                    mudar_idade(id)

                elif opcao == "2":

                    mudar_senha(id)                            
                        
                else:

                    break                 

        elif opcao == "2":

            os.system("cls")                   

            if validacao(id) == True:

                while True:

                    confirmar=erro_ctrl("Deseja confirmar?(S/N):")

                    if confirmar.lower() != "s" and confirmar.lower() != "n":

                        os.system("cls")

                        print("Opção invalida")

                        continue

                    else:

                        break                    

                if confirmar.lower() == "s":

                    os.system(f"rmdir usuarios\\{id} /s /q")

                    print("Usuario foi removido com sucesso")

                    os.system("pause")

                    exit()

                else:

                    print("Cancelado")                   
                                
        else:

             break           