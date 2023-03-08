from limpar import *
from classes import *
from Criar_Aluno import criar_aluno

def criar_turma(turmas):
    #escolher nome da nova turma
    n=len(turmas)+1
    nova_turma=f"Turma {n}"
    while nova_turma in turmas:
        n+=1
        nova_turma=f"Turma {n}"
    
    limpar()   
    print(f"A turma {nova_turma} vai ser criada!")
    
    
    turma=Turma(nova_turma)
    aluno=criar_aluno()
    if aluno == None:
        return
    
    turma.adicionar_aluno(aluno)
    turmas.append(turma)
    limpar()
    
    print(f"Turma {nova_turma} foi criada")
    continuar=input("Precione enter para continuar...")
    return
