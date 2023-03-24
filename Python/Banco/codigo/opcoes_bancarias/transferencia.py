import os
from codigo.validacoes.importar_ctrl_c import erro_ctrl
from codigo.opcoes_bancarias.transferir import transferir
from codigo.validacoes.validacao_transferencia import validar_transferencia
    
def transferencia(id_usuario):
    os.system("cls")
    conta_transferencia=erro_ctrl("Digite a conta para fazer a tranferencia:")
    if os.path.exists(f"usuarios\\{conta_transferencia}") == True:
        if conta_transferencia != id_usuario:
            os.system("cls")

            while True:
                try:                
                    valor_transferencia=erro_ctrl("Informe o valor para a transefrencia:")
                    os.system("cls")
                    valor_transferencia=float(valor_transferencia)
                    break

                except:
                    print(f"{valor_transferencia} Invalido") 
                    continue     

            valor_transferencia=float(valor_transferencia)
            os.system("cls")

            if validar_transferencia(id_usuario,valor_transferencia)== True:
                transferir(id_usuario,valor_transferencia,conta_transferencia)
                print(f"Transefrencia de R$ {valor_transferencia} foi realizado.")
                os.system("pause")
            
            else:
                print("Não foi possivel efetuar a transferencia")
                os.system("pause")
                
        else:
            os.system("cls")
            print("Você não pode transferir para a propria conta")
            os.system("pause")
    else:
        os.system("cls")
        print("Conta nao existente.")
        os.system("pause")
