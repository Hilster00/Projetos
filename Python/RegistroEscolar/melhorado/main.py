import os
from classes import *
from limpar import *
from Adicionar_Aluno import *
from Remover_Turma import remover_turma
from Remover_Aluno import remover_aluno
from Visualisar_Turmas import visualisar_turmas
from Criar_Turma import criar_turma

turmas=list()
segredo=False

while True:
    limpar()
    
    #menu principal
    print("\n(1) Adicionar uma nova Turma")
    print("\n(2) Adicionar uma novo Aluno")
    print("\n(3) Remover Turma")
    print("\n(4) Remover Aluno")
    print("\n(5) Visualizar Alunos/Turmas")
    print("\n Digite 'Sair' para encerrar o programa")
    #comando secreto
    if segredo == True:
        print("\nTESTE7232 comando secreto")
    opcao=input("\n\nDigite a opcao desejada:")
    
    if opcao == "TESTE7232" and segredo==True:
        limpar()
        print("TESTE")
        for turma in turmas:
            visualisar_turmas([turma])
        print(f"Quantidade de turmas:{len(turmas)}")
        continuar=input()

    elif opcao.title == "Sair":
        break
    
    elif opcao == "1":
        criar_turma(turmas)
        
    elif opcao == "2":
        adicionar_aluno(turmas)
        
    elif opcao == "3":
        remover_turma(turmas)
        
    elif opcao == "4":
        remover_aluno(turmas)
        
    elif opcao == "5":
        visualisar_turmas(turmas)
        
    elif opcao == "Hilster":
       segredo=not(segredo)
       
    elif opcao.title() == "Sair":
        break
    else:
        limpar()
        print("Opção invalida!")
        continuar=input()
