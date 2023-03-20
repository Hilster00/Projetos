import os
os.system("title Desafio Final")
cor=input("Deseja alterar a cor da tela?:")
if (cor.upper())[0] == "S":      
   os.system("color 03")
   

#mensagens gerais
mensagem_all="Nome invalido."
nexiste="Arquivo não existe."

pastas_criadas=[]

def sair_mensagem():
   mensagem_00_00="\nDigite 'sair' para sair."
   print(mensagem_00_00)

def continuar():
    os.system("pause")
    
def limpar():
    os.system("cls")
    
def tela():
    limpar()
    print("Criar pastas         (1)")
    print("Ver pastas criadas   (2)")
    print("Criar arquivos       (3)")
    print("Renomear arquivos    (4)")
    print("Remover arquivos     (5)\n")
    sair_mensagem()

#programas

    
def programa_1():
    while True:
        limpar()
        sair_mensagem()
        mensagem_01="\n\nDigite o nome da pasta a ser criada:"
        nome_pasta=input(mensagem_01)
        if os.path.isdir(nome_pasta):
            limpar()
            mensagem_01_00=f"Pasta {nome_pasta} já existe"
            print(mensagem_01_00)
            continuar()
        else:
            if nome_pasta.upper() == "SAIR":
                break
            if nome_pasta=="":
               limpar()
               print(mensagem_all)
               continuar()
               continue
            limpar()
            os.mkdir(f"{nome_pasta}")
            pastas_criadas.append(nome_pasta)
            mensagem_03=f"{nome_pasta} foi criada com sucesso."
            print(mensagem_03)
            continuar()
            



def programa_2():
   while True:
      mensagem_02_0="Nenhuma pasta foi criada"
      mensagem_02_1="As pastas que foram criadas agora são as seguintes.\n"
      mensagem_02_2="Digite o nome da pasta que quer acessar:"
      mensagem_02_3="Pastas existentes.\n"
      limpar()
      if pastas_criadas != []:
         print(mensagem_02_1)
         for x in pastas_criadas:
            print(x)
         print("\n")
         continuar()
         limpar()
         print(mensagem_02_3)
         os.system("tree")
         continuar()
      else:
         limpar()
         print(mensagem_02_0)
         continuar()
         break
      while True:
         limpar()
         sair_mensagem()
         
         nome_pasta=input(mensagem_02_2)
         if os.path.isdir(nome_pasta):
            limpar()
            os.listdir(f"{nome_pasta}")
            continuar()
            break
         else:
            if nome_pasta.upper() == "SAIR":
               break
            else:
               limpar()
               mensagem_02_0=f"Pasta {nome_pasta} não existe."
               print(mensagem_02_0)
               continuar()
               continue
      if nome_pasta.upper() == "SAIR":
               break



def programa_3():
   while True:
      mensagem_03_0="Digite o nome do arquivo a ser criado:"
      limpar()
      sair_mensagem()
      novo_arquivo=input(mensagem_03_0)
      if novo_arquivo.upper() == "SAIR":
         break
      if novo_arquivo == "" or novo_arquivo == ".":     
         limpar()
         print(mensagem_all)
         continuar()
         continue
      novo_arquivo=novo_arquivo.split(".")
      novo_arquivo=novo_arquivo[0]
      novo_arquivo+=".txt"
      if os.path.exists(novo_arquivo):
         limpar()
         mensagem_03_1=f"Arquivo {novo_arquivo} já existe"
         print(mensagem_03_1)
         continuar()
         continue
      mensagem_03_2=f"Arquivo {novo_arquivo} criado com sucesso."
      limpar()
      print(mensagem_03_2)
      animes=open(novo_arquivo,"w")      
      continuar()
         

def programa_4():
   while True:
      mensagem_04_0="Digite o nome do arquivo a ser renomeado:"
      mensagem_04_1="Digite o novo nome do arquivo:"
      limpar()
      sair_mensagem()
      arquivo_renomear=input(mensagem_04_0)
      if arquivo_renomear.upper() == "SAIR":
         break
      if arquivo_renomear == "" or arquivo_renomear == ".":     
         limpar()
         print(mensagem_all)
         continuar()
         continue
      arquivo_renomear=arquivo_renomear.split(".")
      arquivo_renomear=arquivo_renomear[0]
      arquivo_renomear+=".txt"
      if not(os.path.exists(arquivo_renomear)):
         limpar()
         print(nexiste)
      else:
         while True:
            limpar()
            sair_mensagem()
            novo_nome=input(mensagem_04_1)
            if novo_nome.upper() == "SAIR":
               break
            if novo_nome == "" or novo_nome == ".":     
               limpar()
               print(mensagem_all)
               continuar()
               continue
            novo_nome=novo_nome.split(".")
            novo_nome=novo_nome[0]
            novo_nome+=".txt"
            if os.path.exists(novo_nome):
               continue
            rename=f"move {arquivo_renomear} {novo_nome}"
            os.system(rename)
            limpar()
            rename=f"Arquivo {arquivo_renomear} foi renomeado"
            rename+=f" para {novo_nome} com sucesso."
            print(rename)
            continuar()
            break
         if novo_nome.upper() == "SAIR":
               break
         continue
            
            
      

def programa_5():
   while True:
      mensagem_05_0="Digite o nome do arquivo que deseja remover:"
      limpar()
      sair_mensagem()
      arquivo_remover=input(mensagem_05_0)
      if arquivo_remover.upper() == "SAIR":
         break
      if arquivo_remover== "" or arquivo_remover == ".":     
         limpar()
         print(mensagem_all)
         continuar()
         continue
      arquivo_remover=arquivo_remover.split(".")
      arquivo_remover=arquivo_remover[0]
      arquivo_remover+=".txt"
      if os.path.exists(arquivo_remover):
         limpar()
         os.remove(arquivo_remover)
         mensagem_05_1=f"Arquivo {arquivo_remover} foi removido com sucesso."
         print(mensagem_05_1)
         continuar()
         continue     
      limpar()
      print(nexiste)
      continuar()
      
      

#Programa final
while True:
    mensagem_00="Digite a opção desejada:"
    tela()
    opcao=input(mensagem_00)
    if opcao.isnumeric() == False:
        if opcao.upper() == "SAIR":
            break
        else:
            limpar()
            mensagem_00=f"Opção {opcao} não é valido"
            print(mensagem_00)
            continuar()            
            continue
    else:
        if opcao == "1":
           programa_1()
        elif opcao == "2":
           programa_2()
        elif opcao == "3":
           programa_3()
        elif opcao == "4":
           programa_4()
        elif opcao == "5":
           programa_5()
        else:
            limpar()
            mensagem_00=f"Opção {opcao} não é valido"
            print(mensagem_00)
            continuar()            
            continue



limpar()
os.system("color 09")
despedida="\n\t\t\t\tTenha um bom dia.\n\t\t\t\t    até depos"
despedida+="\n"*21
os.system("title SENHOR_H")
print(despedida)

continuar()  
