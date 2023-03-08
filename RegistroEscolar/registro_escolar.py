import os

turmas=[]
numero_de_turmas=0
nomes=[]
sexo=[]
nota1=[]
nota2=[]
segredo=False
turma_escolhida=""

aparelho="cls"
def limpar():
    os.system(aparelho)
    print('Digite "sair" para sair.')
def limp():
      os.system(aparelho)
while True:
    limpar()
    turmas=sorted(turmas)
    print("\n\n\n(1) Adicionar uma nova Turma")
    print("\n(2) Adicionar uma novo Aluno")
    print("\n(3) Remover Turma")
    print("\n(4) Remover Aluno")
    print("\n(5) Visualizar Alunos/Turmas")
    
    if segredo == True:
        print("\nTESTE7232 comando secreto")
    opcao=input("\n\n\nDigite a opcao desejada:")
    if opcao.title()=="Android":
          aparelho="clear"
    if opcao == "TESTE7232":
        limpar()
        print("TESTE")
        print(f"{turmas}\n{nomes}\n{nota1}\n{nota2}\n{numero_de_turmas}")
        print(sexo)
        continuar=input()
        continue
    if opcao.title == "Sair":
        break
    elif opcao == "1":
        limpar()
        teste=0
        nova_turma="Turma 1"
        while nova_turma in turmas:
            teste+=1
            nova_turma=f"Turma {teste}"
        numero_de_turmas+=1
        print(f"A turma {nova_turma} vai ser criada!")
        novo_aluno=input("\nDigite o nome do novo aluno:")
        while novo_aluno.isalpha() == False:
            novo_aluno=input("Digite um nome do novo aluno valido:")
        novo_aluno=novo_aluno.title()
        
        if novo_aluno == "Sair":
            numero_de_turmas-=1
            continue
        novo_aluno=f"{novo_aluno} {nova_turma}"
        novo_sexo="g"
        while True:
            limpar()
            novo_sexo=input("Informe o sexo (M) ou (F):")
            novo_sexo=novo_sexo.title()
            if novo_sexo[0] == "M":
                novo_sexo="Masculino"
                break
            elif novo_sexo[0]=="F":
                novo_sexo="Feiminino"
                break
            elif novo_sexo == "Sair":
                break
        if novo_sexo == "Sair":
                numero_de_turmas-=1
                continue              
                
        not1="a"
        while True:
              while not1.isnumeric() == False:
                  limpar()
                  not1=input("Digite a primeira nota:")
                  if not1.title() == "Sair":
                      not1="Sair"
                      break
              
              not1=float(not1)
              if not1 == "Sair":
                    break
              if not1 > 10:
                         not1="a"
              else:
                    break
        if not1 == "Sair":
            numero_de_turmas-=1
            continue
        not1=float(not1)
        not2="a"
        while True:
              while not2.isnumeric() == False:
                  limpar()
                  not2=input("Digite a segunda nota:")
                  if not2.title() == "Sair":
                      not2="Sair"
                      break
              
              not2=float(not2)
              if not2 == "Sair":
                    break
              if not2 > 10:
                         not2="a"
              else:
                    break
        if not2 == "Sair":
            numero_de_turmas-=1
            continue
        nomes.append(novo_aluno)
        not2=float(not2)
        sexo.append(novo_sexo)
        nota1.append(not1)
        nota2.append(not2)
        turmas.append(nova_turma)
        limp()
        print(f"Turma {nova_turma} foi criada")
        continuar=input("Precione enter para continuar...")
        
    elif opcao == "2":
        if turmas == []:
            print("Primeiro registre uma turma!")
            continuar=input("Precione enter para continuar...")
            limpar
        else:
            turma_escolhida="0"
            while True:
                if turma_escolhida == "Sair":
                            break
                limp()
                
                
                
                
                
                for x in turmas:
                        print(x)
                        escolha="2"
                continuar=input("Precione enter para continuar...")
                
                if numero_de_turmas == 1:
                        turma_escolhida=turmas[0]
                else:
                      turma_escolhida="RANDOM"
                while turma_escolhida not in turmas:
                            turma_escolhida=input("Digite o nome da turma a ser adicionado novos alunos.\nEx: Turma 1\n:")
                            turma_escolhida=turma_escolhida.title()
                            if turma_escolhida == "Sair":
                                break
                if turma_escolhida == "Sair":
                      continue
                contagem_alunos=0
                for x in nomes:
                        if x.endswith(turma_escolhida):
                         contagem_alunos+=1   
                while True:
                        limpar()
                        print(turma_escolhida)    
                        aluno_nome="a2"
                        while aluno_nome.isalpha() == False:
                            aluno_nome=input(f"Digite o nome do novo aluno da turma {turma_escolhida}:")                            
                            aluno_nome=aluno_nome.title()
                            
                            
                        if aluno_nome == "Sair" :
                            break
                        aluno_nome=f"{aluno_nome} {turma_escolhida}"
                        novo_sexo="g"
                        while (novo_sexo!= "M" and novo_sexo!="F"):
                            limpar()
                            novo_sexo=input("Informe o sexo (M) ou (F):")
                            novo_sexo=novo_sexo.title()
                            if novo_sexo == "Sair":
                                break
                            novo_sexo=novo_sexo[0]
                        if novo_sexo=="Sair":
                            break
                        if novo_sexo == "M":
                            novo_sexo="Masculino"
                        else:
                            novo_sexo="Feiminino"
        
                        not1="a"
                        while True:
                              while not1.isnumeric() == False:
                                  limpar()
                                  not1=input("Digite a primeira nota:")
                                  if not1.title()== "Sair":
                                      not1="Sair"
                                      break
                              if not1 == "Sair":
                                      break
                              not1=float(not1)
                              if not1 > 10:
                                          not1="a"
                              else:
                                    break
                        if not1 == "Sair":
                                break

                        
                        not2="a"
                        while True:
                              while not2.isnumeric() == False:
                                  limpar()
                                  not2=input("Digite a Segunda nota:")
                                  if not2.title()== "Sair":
                                      not2="Sair"
                                      break
                              if not2 == "Sair":
                                      break
                              not2=float(not2)
                              if not2 > 10:
                                          not2="a"
                              else:
                                    break
                        if not2 == "Sair":
                                break

                        
                        nomes.append(aluno_nome)
                        sexo.append(novo_sexo)
                        nota1.append(not1)
                        nota2.append(not2)
                        contagem_alunos+=1
                        os.system(aparelho)
                        print(f"Aluno {aluno_nome} foi adicionado a turma {turma_escolhida}")
                        continuar=input("Precione enter para continuar...")
                        if contagem_alunos == 40:
                            limpar()
                            print("Limite de alunos atingido!")
                            continuar=input("Precione enter para continuar...")
                            break
                break
                    
    elif opcao == "3":
        if numero_de_turmas != 0:
            limpar()
            turma_escolhida=""
            if numero_de_turmas == 1:
                turma_escolhida=turmas[0]
            else:
                limpar()
                print("\nEssas são todas as turmas registradas\n")
                for x in turmas:
                      print(f"\n{x}")
                while turma_escolhida not in turmas:
                    
                    turma_escolhida=input("Digite a turma a ser removida:")
                    turma_escolhida=turma_escolhida.title()
                    if turma_escolhida == "Sair":
                        break                
                    limpar()
                    if turma_escolhida not in turmas:
                          print("Turma não existente!")
                          continuar=input()
                          continue
                
            while True:                
                if turma_escolhida=="Sair":
                    break
                limpar

                
                
                
                b=[]
                for x in nomes:
                    b.append(x)
                n=0
                for x in b:
                    if x.endswith(turma_escolhida):
                        
                        nomes.remove(nomes[n])
                        sexo.remove(sexo[n])
                        nota1.remove(nota1[n])
                        nota2.remove(nota2[n])
                        continue
                    n+=1
                   
                   
                
                
                numero_de_turmas-=1
                turmas.remove(turma_escolhida)
                limp()
                print(f"A turma {turma_escolhida} foi removida")
                continuar=input("Precione enter para continuar...")
                break
        else:
            limp()
            print("Não existe turmas registradas!")
            continuar=input("Precione enter para continuar...")
            limpar()
            
    elif opcao == "4":
        if numero_de_turmas != 0:
            limpar()
            while True:
                if numero_de_turmas == 1:
                    turma_escolhida=turmas[0]
                else:
                    turma_escolhida=input("Digite o nome da turma que deseja ermover os alunos:")
                    turma_escolhida=turma_escolhida.title()                
                if turma_escolhida not in turmas:
                    limpar()
                    if turma_escolhida == "Sair":
                        break                    
                    print("Turma não existente!")
                    continue
                numero_de_alunos=0               
                for x in nomes:
                    if x.endswith(turma_escolhida)==True:
                        numero_de_alunos+=1
                n=0
                nome_escolhido="f2" 
               
                while True:
                    limpar()                                     

                    while nome_escolhido.isalpha() == False:
                        nome_escolhido=input(f"Digite o nome do aluno a ser removido da turma {turma_escolhida}:")
                        nome_escolhido=nome_escolhido.title()
                    
                    if nome_escolhido == "Sair":
                        break
                    
                    nome_escolhido=f"{nome_escolhido} {turma_escolhida}"
                    if nome_escolhido in nomes:
                        n=nomes.index(nome_escolhido)       
                        nomena=nomes[n]
                        nomes.remove(nomena)
                        sexona=sexo[n]
                        sexo.remove(sexona)
                        notana=nota1[n]
                        nota1.remove(notana)
                        notana2=nota2[n]
                        nota2.remove(notana2)
                        numero_de_alunos-=1
                    else:
                        limpar()                
                        print(f"Nome {nome_escolhido} não encontrado!")
                        continuar=input("Precione enter para continuar...")
                    limp()
                    nome_escolido=nome_escolhido.split(turma_escolhida)
                    
                   
                    print(f"O aluno {nome_escolhido[0]} foi removido")
                    os.system(f"msg * O aluno {nome_escolhido[0]} foi removido")
                    continuar=input("Precione enter para continuar...")                    
                    if numero_de_alunos == 0:
                            turmas.remove(turma_escolhida)
                            numero_de_turmas-=1
                            limp()
                            print(f"A turma {turma_escolhida} foi removida")
                            continuar=input("Precione enter para continuar...")
                            break
                    
                    
                break
                    
        
    elif opcao == "5":
        limpar()
        for x in turmas:
            print(f"\n{x}")
        while True:

            continuar=input("Precione enter para continuar...")
            turma_escolhida=""
            if numero_de_turmas == 1:
                turma_escolhida=turmas[0]
            
            elif numero_de_turmas == 0:
                print("Não existe turmas")
                continuar=input()
                break
        
            while turma_escolhida not in turmas:
                
                turma_escolhida=input("Digite a turma que deseja ver os alunos:")
                turma_escolhida=turma_escolhida.title()
                if turma_escolhida == "Sair":
                      break
            if turma_escolhida == "Sair":
                      break
            limpar()
            n=0
            media=0
            media_da_turma=0
            numero_de_alunos=0
      
            for x in nomes:
                if x.endswith(turma_escolhida):
                    nome_de_exibicao=x.split(turma_escolhida)
                    nome_de_exibicao=nome_de_exibicao[0]
                    numero_de_alunos+=1
                    media=(nota1[n]+nota2[n])/2
                    media_da_turma+=media
                    print(f"\n{nome_de_exibicao} aluno da turma {turma_escolhida}, do sexo {sexo[n]} com a 1ª e 2ª nota sendo {nota1[n]}, {nota2[n]}\nrespectivamente e com a média {media}.")
                n+=1
            media_da_turma/=numero_de_alunos
            print(f"\nE a turma {turma_escolhida} tem {numero_de_alunos} alunos, com a média total da sala sendo {media_da_turma}.")
            continuar=input("Precione enter para continuar...")
            break


    elif opcao == "Hilster":
        if segredo == True:
            segredo=False
        else:
            segredo=True
    elif opcao.title() == "Sair":
        break
    else:
        limpar()
        print("Opção invalida!")
        continuar=input()
