from limpar import *

def remover_turma(turmas):
    limpar()
    
    if len(turmas) == 0:
        print("Não existe turmas registradas!")
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
        turma=input("Digite o nome da turma a ser removida.\nEx: Turma 1\n:")
        turma=turma.title()
        if turma == "Sair":
            return
    turma=turmas[lista.index(turma)]
    
    #remocao da turma
    turmas.remove(turma)
    print(f"A turma {turma.nome} foi removida")
    continuar=input("Precione enter para continuar...")
