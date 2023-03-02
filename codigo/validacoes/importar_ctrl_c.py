#importar_ctrl_c

def erro_ctrl(mensagem):

    try:

        informacao=input(mensagem)
    except:
            
        informacao=""
    
    return informacao