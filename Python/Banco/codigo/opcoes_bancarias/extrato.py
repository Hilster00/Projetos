#extrato
import os

def extrato(id_usuario):

    os.system("cls")
    nome_idade=open(f"usuarios\\{id_usuario}\\nome.txt","r")
    nome_idade_limpo=nome_idade.readlines()
    nome_idade_limpo[0]=nome_idade_limpo[0].split("\n")
    nome_idade_limpo[0]=nome_idade_limpo[0][0]
    dinheiro_conta=open(f"usuarios\\{id_usuario}\\dinheiro.txt","r")
    dinheiro_limpo=dinheiro_conta.readlines()
    dinheiro_limpo=float(dinheiro_limpo[0])
    dinheiro_conta.close()
    nome_idade.close()

    print(f"Usuario {nome_idade_limpo[0]} idade {nome_idade_limpo[1]} anos")
    print("\n")
    print(f"Você possui R${dinheiro_limpo} na conta")
    print("\n"*15)

    os.system("pause")
