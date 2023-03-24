#opcoes_bancarias

import os
from codigo.opcoes_bancarias.saque import saque
from codigo.validacoes.validacao import validacao
from codigo.opcoes_bancarias.extrato import extrato
from codigo.opcoes_bancarias.deposito import deposito
from codigo.opcoes_bancarias.transferencia import transferencia
from codigo.telas.tela_opcoes_bancarias import tela_opcoes_bancarias

def opcoes_bancarias(id):
    while True:
        opcao=tela_opcoes_bancarias()

        if opcao != "5":                 
            if validacao(id) == False:
                continue

        if opcao =="1":
            saque(id)

        elif opcao == "2":
            deposito(id)

        elif opcao == "3":    
            if len(os.listdir("usuarios\\")) != 1:
                transferencia(id)                 

            else:
                os.system("cls")
                print("Nao existe outra conta para faer transferencia")
                os.system("pause")
                
        elif opcao =="4":            
            extrato(id)

        elif opcao == "5":
            break
