#cadastro

import os
from codigo.cadastros.criar_id import criar_id
from codigo.validacoes.validar_cpf import validar_cpf
from codigo.validacoes.importar_ctrl_c import erro_ctrl
from codigo.validacoes.validar_idade import validar_idade
from codigo.cadastros.criar_arquivos import criar_arquivos_usuario

def cadastrar():

    informacoes=["nome do usuario","senha"]

    quantidade_caracteres=[2,5]

    tipo_da_informacao_texto=[True,False]

    novo_usuario={}

    os.system("cls")

    novo_usuario["idade"]=validar_idade()

    if novo_usuario["idade"] >= 18:

        os.system("cls")

        for iten in informacoes:

            while True: 

                print("\n")       
            
                novo_usuario[iten]=erro_ctrl(f"Informe o {iten} do novo usuario:")

                os.system("cls")

                if len(novo_usuario[iten]) < quantidade_caracteres[informacoes.index(iten)]:

                    print(f"Quantidade de digitos invalido\ndeve ter pelomenos {quantidade_caracteres[informacoes.index(iten)]} digitos")
                    
                else:
                    
                    if iten != "senha":

                        if novo_usuario[iten].isalpha() == tipo_da_informacao_texto[informacoes.index(iten)]:

                            break

                        os.system("cls")

                        print(f"{novo_usuario[iten]} invalido como {iten}")
                    else:

                        break

        os.system("cls")

        novo_usuario["cpf"]=validar_cpf()

        while True:

            novo_id=criar_id()            

            if os.path.exists(f"usuarios\\{novo_id}") == False:

                break
                
        nova_pasta_usuario=novo_id.upper()
        
        os.system("cls")        

        nome=novo_usuario["nome do usuario"].title()        
        
        confirmar=erro_ctrl(f"Confirma o novo cadastro do {nome} (S/N):").lower()

        if confirmar.lower() == "s" or confirmar.lower() == "sim":
                    
            mensagem=criar_arquivos_usuario(nova_pasta_usuario,novo_usuario,nome,novo_id)

        else:

            mensagem=f"Usuario {nome} não foi criado."   

        os.system("cls") 

        print(mensagem)

        os.system("pause")

    else:

        os.system("cls")

        print("Lamento, mas so maiores de 18 podem fazer uma conta nesse banco!")

        os.system("pause")