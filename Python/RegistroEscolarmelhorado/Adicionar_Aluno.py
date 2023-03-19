from limpar import *
from classes import *
from Criar_Aluno import criar_aluno

def adicionar_aluno(turmas):
    limpar()
    if len(turmas) == 0:
        print("Primeiro registre uma turma!")
        continuar=input("Precione enter para continuar...")
        return
    
    #listagem de nomes de turmas
    print("Lista de turmas:",end="")
    lista=list()
    for x in turmas[:-1]:
        print(f"{x.nome},",end="")
        lista.append(x.nome)
    print(f"{turmas[-1].nome}")  
    lista.append(turmas[-1].nome)
    
    #selecionando a primeira turma, caso só tenha uma cadastrada
    turma="RANDOM"
    if len(turmas) == 1:
        turma=lista[0]
        
    #escolha da turma para adicionar alunos
    while turma not in lista:
        turma=input("Digite o nome da turma a ser adicionado novos alunos.\nEx: Turma 1\n:")
        turma=turma.title()
        if turma == "Sair":
            return
        
    turma=turmas[lista.index(turma)]
    
    #cadastro de novos alunos em loop
    while True:
        
        limpar()
        print(turma.nome)    
        aluno=criar_aluno()
        if aluno == None:
            return
        
        #adionando novo aluno a turma
        turma.adicionar_aluno(aluno) 
        print(f"Aluno {aluno.nome} foi adicionado a turma {turma.nome}")
        continuar=input("Precione enter para continuar...")
        
        #verificacao se o limite de cadastros foi atingido
        if turma.quantidade_alunos() == 40:
            limpar()
            print("Limite de alunos atingido!")
            continuar=input("Precione enter para continuar...")
            return
