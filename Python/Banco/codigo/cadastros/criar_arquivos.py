#criar_arquivos_usuario
import os

def criar_arquivos_usuario(nova_pasta_usuario,novo_usuario,nome,novo_id):

    os.system(f"mkdir usuarios\\{nova_pasta_usuario}")

    #____________________________________________________________________________________
    try:
        nome_usuario=open(f"usuarios\\{nova_pasta_usuario}\\nome.txt", "a")
        nome_usuario.write(novo_usuario["nome do usuario"].title())
        nome_usuario.write(f"\n{novo_usuario['idade']}")
        nome_usuario.close()
        
        #____________________________________________________________________________________

        senha_usuario=open(f"usuarios\\{nova_pasta_usuario}\\senha.txt", "a")
        senha_usuario.write(novo_usuario["senha"])
        senha_usuario.close()

        #____________________________________________________________________________________

        dinheiro_usuario=open(f"usuarios\\{nova_pasta_usuario}\\dinheiro.txt", "a")
        dinheiro_usuario.write("0")
        dinheiro_usuario.close()

        #____________________________________________________________________________________

        cpf_usuario=open(f"usuarios\\{nova_pasta_usuario}\\cpf.txt", "a")
        cpf_usuario.write(novo_usuario["cpf"])
        cpf_usuario.close() 
        mensagem=f"Usuario {nome} cadastrado com sucesso.\nSeu id é {novo_id.upper()}"
                  
    except:
        mensagem=f"Usuario {nome} não foi criado com sucesso."
    
    return mensagem
