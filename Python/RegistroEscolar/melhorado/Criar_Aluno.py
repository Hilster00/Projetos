from limpar import *
from classes import Aluno

def criar_aluno():
    limpar()
    
    #nome do novo aluno
    nome=input("\nDigite o nome do novo aluno:")
    nome=nome.title()
    
    #caso deseje cancelar criacao da nova turma
    if nome == "Sair":
        return None
    
    #receber sexo do aluno
    while True:
        limpar()
        sexo=input("Informe o sexo (M) ou (F):")
        if sexo[0].title() in ["M",'F']:
            sexo="Masculino" if sexo[0].title()=="M" else "Feiminino"
            break
        elif sexo.title() == "Sair":
            return None
        
    #recebendo as notas
    notas=list()
    for i in range(2):
        while True:
            try:
                limpar()
                nota=input(f"Digite a nota {i+1}:")
                nota=float(nota)
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                continue
            except:
                if nota.title() == 'Sair':
                    return None
    
    novo_aluno=Aluno(nome,sexo,notas)
    return novo_aluno
