from limpar import *
from classes import *

def visualisar_turmas(turmas):
    limpar()
    
    if len(turmas) == 0:
        print("Não existe turmas registradas!")
        continuar=input("Precione enter para continuar...")
        return
        
    #listagem de nomes de turmas
    print("Lista de turmas:",end="")
    lista=[x.nome for x in turmas]
    for x in lista[:-1]:
        print(f"{x},",end="")
    print(f"{lista[-1]}")  
        
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

    lista=turma.lista_alunos()
    media_da_turma=0
    
    limpar()
    for aluno in lista:
        notas=aluno.notas
        media=sum(notas)/2
        print(f"\n{aluno.nome} aluno da turma {turma.nome},")
        print(f"do sexo {aluno.sexo}, com a 1ª e 2ª nota sendo {notas[0]}, {notas[1]}",end="")
        print(f"respectivamente,e com a média {media}.")
        media_da_turma+=media
    
    media_da_turma/=len(lista)
    print(f"\nE a turma {turma.nome} tem {len(lista)} alunos,\n")
    print(f"com a média total da sala sendo {media_da_turma}.")
    continuar=input("Precione enter para continuar...")
