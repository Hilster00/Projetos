import os
mensagem = ""

#Lista as pastas e arquivos do diretório
diretorio = 'C:\\'
arquivos_pasta = os.listdir(diretorio)
nome_arquivo = 'C:\\Caixa\\produtos.txt'
nome_arquivo_2 = 'C:\\Caixa\\precos.txt'

#Verifica se a pasta onde fica os produtos existe e se não existir cria uma
if 'Caixa' not in arquivos_pasta:
    diretorio = 'C:\\Caixa'
    os.mkdir(diretorio)

#Cria um arquivo ".txt" caso ele não exista
diretorio_2 = 'C:\\Caixa'
arquivos_pasta_2 = os.listdir(diretorio_2)       
if 'produtos.txt' not in arquivos_pasta_2 or 'precos.txt' not in arquivos_pasta_2:
    
    #Armazena os produtos
    arquivo = open(nome_arquivo, 'w')
    arquivo.write('Arroz\n')           
    arquivo.write('Leite\n')           
    arquivo.write('Bolacha\n')           
    arquivo.write('Feijão\n')
    arquivo.close()
    
    #Armazena os preços
    arquivo = open(nome_arquivo_2, 'w')
    arquivo.write('15.99\n')
    arquivo.write('3.89\n')
    arquivo.write('1.99\n')
    arquivo.write('10.95\n')
    arquivo.close()

#Armazeno os produtos e preços em uma lista
arquivo = open('C:\\Caixa\\produtos.txt', 'r')
arquivo_2 = open('C:\\Caixa\\precos.txt', 'r')
conteudo_arquivo = arquivo.readlines()
conteudo_arquivo_2 = arquivo_2.readlines()
arquivo.close
arquivo_2.close 

#Retiro os "\n" da lista dos produtos
produtos_limpos = []
for informacoes in conteudo_arquivo:
    quebra_de_linha = informacoes.split('\n')
    produtos_limpos.append(quebra_de_linha[0])

#Retiro os "\n" da lista dos precos
precos_limpos = []
for informacoes in conteudo_arquivo_2:
    quebra_de_linha = informacoes.split('\n')
    precos_limpos.append(quebra_de_linha[0])

while(True):
    os.system("cls")
    print('\nDigite "sair" para fechar o programa.\nQual ambiente deseja utilizar?\n(1)Passar produtos (2)Modificar produtos')

    opcao = input('\nDigite a opção desejada: ')

    if opcao == '1':                   
        #Lista dos preços e produtos que o cliente comprar
        produtos_cliente = []
        precos_cliente = []

        while(True):
            os.system("cls")
            
            #Printo os produtos
            print('Digite "Sair" para voltar ao menu anterior.')
            print(f'\nProdutos cadastrados no sistema:')      
            for x in produtos_limpos:
                print(f"{x}\tR${precos_limpos[produtos_limpos.index(x)]}")
            print('Para finalizar a compra digite "Finalizar".')
            
            produto = input('\nDigite o nome do produto: ')    

            #Verifica se o produto foi cadastrado
            if produto.title() in produtos_limpos:
                
                #Printa o produto e o preço do mesmo e o adiciona na lista
                print(f"{produto.title()}\tR${precos_limpos[produtos_limpos.index(produto.title())]}")
                produtos_cliente.append(produto.title())
                precos_cliente.append(precos_limpos[produtos_limpos.index(produto.title())])
                os.system('pause')

            elif produto.title() == "Finalizar":
                if len(produtos_cliente) < 1:
                    print('Nenhum produto foi adicionado; adicione ao menos um produto para finalizar a compra.')
                    os.system('pause')
                    continue    
                
                #Calculo os produtos
                total = 0
                for x in precos_cliente:                 
                    x = float(x)
                    total += x 

                while True:
                    os.system("cls")
                    
                    #Printo os produtos
                    print("\nProdutos comprados:")
                    for x in produtos_cliente:
                        print(f"{x}\tR${precos_cliente[produtos_cliente.index(x)]}")
                    print(f'Total: R${total:.2f}')
                    pagamento = input('Digite a quantia de dinheiro que será usada para a compra: ')

                    #Verifica se o número é float
                    if pagamento.isnumeric() == False:
                        teste_de_float = 0
                        vezes = 0
                        ponto = 0
                        
                        for x in pagamento: 
                            if x.isnumeric() == True:
                                teste_de_float+=1
                            
                            else:
                                if x == ".":
                                    if ponto == 0:
                                        teste_de_float += 1 
                                        ponto += 1
                            vezes+=1

                    if pagamento.isnumeric() == True or vezes == teste_de_float:
                            #Cast para float
                            pagamento = float(pagamento)
                            
                            if pagamento < total:
                                print('Quantia insufiente!')
                                os.system('pause')
                            
                            #Verfica quais notas devem ser retornadas como troco
                            else:
                                troco = pagamento - total
                                notas_200 = int(troco/200)
                                troco = troco - (notas_200*200)
                                notas_100 = int(troco/100)
                                troco  = troco - (notas_100*100)
                                notas_50 = int(troco/50)
                                troco = troco - (notas_50*50)
                                notas_20 = int(troco/20)
                                troco = troco - (notas_20*20)
                                notas_10 = int(troco/10)
                                troco = troco - (notas_10*10)
                                notas_5 = int(troco/5)
                                troco = troco - (notas_5*5)
                                notas_2 = int(troco/2)
                                troco = troco - (notas_2*2)
                                mensagem = "O Troco deverá ser pago com:"

                                if notas_200 != 0:
                                    if notas_200 == 1:
                                        mensagem = f"{mensagem} {notas_200} nota de 200 reais,"
                                    
                                    else:
                                        mensagem  =f"{mensagem} {notas_200} notas de 200 reais,"

                                if notas_100 != 0:
                                        mensagem = f"{mensagem} {notas_100} nota de 100 reais,"

                                if notas_50 != 0:
                                    mensagem = f"{mensagem} {notas_50} nota de 50 reais,"
                            
                                if notas_20 != 0:
                                    if notas_20 == 1:
                                        mensagem = f"{mensagem} {notas_20} nota de 20 reais,"
                                    
                                    else:
                                        mensagem = f"{mensagem} {notas_20} notas de 20 reais,"

                                if notas_10 != 0:
                                    mensagem = f"{mensagem} {notas_10} nota de 10 reais,"

                                if notas_5 != 0:
                                    mensagem = f"{mensagem} {notas_5} nota de 5 reais,"

                                if notas_2 != 0:
                                    if notas_2 == 1:
                                        mensagem = f"{mensagem} {notas_2} nota de 2 reais,"
                                    
                                    else:
                                        mensagem = f"{mensagem} {notas_2} notas de 2 reais,"

                                if troco != 0:
                                    moeda_1_r = int(troco)
                                    troco = troco - moeda_1_r
                                    troco = troco*100
                                    moeda_50_c = int(troco/50)
                                    troco = troco - (moeda_50_c*50)
                                    moeda_25_c = int(troco/25)
                                    troco = troco - (moeda_25_c*25)
                                    moeda_10_c = int(troco/10)
                                    troco = troco - (moeda_10_c*10)
                                    moeda_5_c = int(troco/5)
                                    troco = troco - (moeda_5_c*5)
                                    moeda_1_c = troco

                                if moeda_1_r != 0:
                                    mensagem = f"{mensagem} {moeda_1_r} moeda de 1 real."

                                if moeda_50_c != 0:
                                    mensagem = f"{mensagem} {moeda_50_c} moedas de 50 centavos."

                                if moeda_25_c != 0:
                                    mensagem=f"{mensagem} {moeda_25_c} moedas de 25 centavos."

                                if moeda_10_c != 0:
                                    if moeda_10_c == 1:
                                        mensagem = f"{mensagem} {moeda_10_c} moeda de 10 centavos."
                                    
                                    else:
                                        mensagem = f"{mensagem} {moeda_10_c} moedas de 10 centavos."

                                if moeda_5_c != 0:
                                    mensagem = f"{mensagem} {moeda_5_c} moeda de 5 centavos."

                                if moeda_1_c != 0:
                                    if int(moeda_1_c) == 1 or moeda_1_c > 0.98 and moeda_1_c < 1:
                                        mensagem = f"{mensagem} 1 moeda de 1 centavo."
                                    
                                    elif moeda_1_c > 1:
                                        mensagem = f"{mensagem} {int(moeda_1_c)} moedas de 1 centavo."
                                os.system("cls")
                
                                troco = pagamento - total
                                
                                print(f'Valor pago pelo cliente: R${pagamento}')
                                print(f'Troco: R${troco:.2f}')
                                print(mensagem)
                                print('Compra finalizada!')
                                produtos_cliente = []
                                precos_cliente = []
                                os.system('pause')
                                break
                                
                    
                    else:
                        print('Digite uma quantia válida.')
                        os.system('pause')

            else:
                if produto.title() == 'Sair':
                    break
                
                else:
                    print('Esse produto não está cadastrado no sistema.')
                    os.system('pause')

    if opcao == '2':

        while True:
            os.system("cls")
            mensagem = ""
            print('Digite "sair" para sair.')
            print("Digite a opção desejada:")
            print("(1) Adicionar um produto")
            print("(2) Editar um produto")
            print("(3) Remover um produto\n\n\n")
            opcao=input("Digite a opção desejada: ")
        
            if opcao == "1":
                mensagem=""
                
                while True:
                    os.system("cls")
                    print(mensagem)
                    print('Digite "sair" para sair.')
                    novo_produto=input("Digite o nome do novo produto: ")
                    
                    if novo_produto.title() in produtos_limpos:
                        mensagem=f"Já existe um produto com o nome {novo_produto.title()}"
                        continue
                    
                    else:
                        os.system("cls")

                        if novo_produto.upper() == "SAIR":
                            break
                        confirmacao=input(f"Deseja confirmar o nome do produto {novo_produto.title()}?: ")
                        
                        if confirmacao.upper()[0] == "N":
                            mensagem=""
                            continue
                    mensagem=""
                    
                    while True: 
                        os.system("cls")
                        print(mensagem)
                        preco_novo_produto=input(f"Digite o preço do produto {novo_produto}: ")
                        
                        if preco_novo_produto.isnumeric() == False:
                            teste_de_float = 0
                            vezes = 0
                            ponto = 0
                            
                            for x in preco_novo_produto: 
                                if x.isnumeric() == True:
                                    teste_de_float+=1
                                
                                else:
                                    if x == ".":
                                        if ponto == 0:
                                            teste_de_float += 1 
                                            ponto += 1
                                vezes+=1

                        if preco_novo_produto.isnumeric() == True or vezes == teste_de_float:
                            os.system("cls")
                            confirmacao=input(f'Deseja confirmar o preço "{novo_produto.title()} R${preco_novo_produto}"?: ')
                            
                            if confirmacao.upper()[0]== "S":
                                                           
                                #Armazena o produto na lista e no arquivo
                                novo_produto = novo_produto.title()
                                produtos_limpos.append(novo_produto)
                                precos_limpos.append(float(preco_novo_produto))
                                arquivo = open(nome_arquivo, 'a')
                                arquivo.write(f'{novo_produto}\n')
                                arquivo.close()
                                arquivo = open(nome_arquivo_2, 'a')
                                arquivo.write(f'{preco_novo_produto}\n')
                                arquivo.close()

                                os.system("cls")
                                print(f'Novo produto "{novo_produto} R${preco_novo_produto}" adicionado com sucesso.')
                                os.system("Pause")
                                break
                            
                            else:
                                mensagem=""
                        
                        else:
                            mensagem=f"O preço {preco_novo_produto} não é valido"
                               
                os.system("pause")
            
            elif opcao == "2":
                mensagem=""
                
                while True:
                    os.system("cls")
                    print('Digite "sair" para sair.')
                    produto=input('Digite o nome do produto a ser editado,\ndigite "lista" para ver a lista de produtos e seus preços: ')
                    
                    if produto.upper()=="LISTA":
                        os.system("cls")
                        for x in produtos_limpos:
                            print(f"{x}\tR${precos_limpos[produtos_limpos.index(x)]}")
                        print('Digite "sair" para sair.')
                        produto=input('Digite o nome do produto a ser editado: ')
                    
                    if produto.title() in produtos_limpos:
                        produto=produto.title()
                        mensagem=""
                        
                        while True:
                            os.system("cls")
                            print(mensagem)
                            print(f'O produto "{produto}" está sendo editado.\n\n')
                            print('Digite "sair" para sair.')
                            print("(1) Para editar o nome.")
                            print("(2) Para editar o preço.\n\n")
                            opcao=input("Digite a opcao que deseja editar: ")
                            
                            if opcao == "1":
                                
                                while True:
                                    os.system("cls")
                                    print('Digite "sair" para voltar ao menu anterior.')
                                    novo_nome=input("Digite o novo nome: ")
                                    
                                    if novo_nome.upper() == "SAIR":
                                        break
                                    
                                    if novo_nome.title() not in produtos_limpos:
                                        confirmacao=input("Deseja confirmar o novo nome :")
                                        
                                        if confirmacao.upper() == "SAIR":
                                            break
                                        
                                        if confirmacao.upper()[0]=="S":
                                            
                                            #Armazeno na lista
                                            produtos_limpos[produtos_limpos.index(produto)]=novo_nome.title()
                                            produto=novo_nome.title()

                                            #Deixo o arquivo vazio para que lista antiga não se repita
                                            i = 0
                                            arquivo = open(nome_arquivo, 'w')
                                            arquivo.write('')
                                            arquivo.close()
                                            
                                            #Armazeno no arquivo
                                            for item in produtos_limpos:
                                                arquivo = open(nome_arquivo, 'a')
                                                arquivo.write(f'{produtos_limpos[i]}\n')
                                                i += 1
                                                arquivo.close()

                                            break
                                    else:
                                        mensagem="Já existe um produto com esse nome."
                                
                                    
                            elif opcao == "2":
                                mensagem=""
                                
                                while True:
                                    os.system("cls")
                                    print(mensagem)
                                    print('Digite "sair" para sair.')
                                    preco=input("Digite o novo preço: ")
                                    
                                    if preco.isnumeric() == False:
                                        
                                        if preco.upper() == "SAIR":
                                            break
                                        
                                        else:
                                            teste_de_float = 0
                                            vezes = 0
                                            ponto = 0
                                            for x in preco:
                                                
                                                if x.isnumeric() == True:
                                                    teste_de_float+=1
                                                
                                                else:
                                                    if x == ".":
                                                        if ponto == 0:
                                                            teste_de_float += 1 
                                                            ponto += 1
                                                vezes += 1   
                                    
                                            mensagem="Preço invalido."
                                    
                                    if preco.isnumeric() == True or vezes == teste_de_float:
                                        
                                        os.system("cls")
                                        confirmacao=input("Deseja confirmar o novo preço?: ")
                                        
                                        if confirmacao.title()[0]=="S":
                                            
                                            precos_limpos[produtos_limpos.index(produto)]=float(preco)
                                            mensagem=""
                                            
                                            #Deixo o arquivo vazio para que a lista antiga não se repita
                                            i = 0
                                            arquivo = open(nome_arquivo_2, 'w')
                                            arquivo.write('')
                                            arquivo.close()
                                            
                                            #Armazeno no arquivo
                                            for item in precos_limpos:
                                                arquivo = open(nome_arquivo_2, 'a')
                                                arquivo.write(f'{precos_limpos[i]}\n')
                                                i += 1
                                                arquivo.close()
                                            
                                            break
                                        
                                        else:
                                            mensagem=""
                            
                            elif opcao.upper() == "SAIR":
                                break
                            
                            else:
                                mensagem="Opção invalida."


                    
                    else:
                        if produto.title() == "Sair":
                            break
                        
                        else:
                            mensagem="Opção invalida."
            
            elif opcao == "3":
                
                mensagem = 'Digite "sair" para voltar ao menu anterior.'
                
                while True:
                    if len(produtos_limpos)==1:
                        break
                    
                    os.system("cls")
                    print(mensagem)
                    print('Digite "lista" para exibir a lista de produtos.')
                    produto=input("Digite o nome do produto a ser removido: ")
                    
                    if produto.upper()=="LISTA":
                        os.system("cls")
                        for x in produtos_limpos:
                            print(f"{x} R${precos_limpos[produtos_limpos.index(x)]}")                       
                        produto=input("Digite o nome do produto a ser removido: ")
                    
                    if produto.title() in produtos_limpos:
                        confirmacao=input(f"Deseja realmente remover o produto {produto.title()} R${precos_limpos[produtos_limpos.index(produto.title())]}?: ")
                        
                        if confirmacao.upper()[0]=="S":
                            
                            #Removo o produto da lista
                            produto=produto.title()
                            precos_limpos.pop(produtos_limpos.index(produto))
                            produtos_limpos.remove(produto)

                            #Deixo o arquivo vazio para que a lista antiga não se repita
                            i = 0
                            arquivo = open(nome_arquivo_2, 'w')
                            arquivo.write('')
                            arquivo.close()
                            
                            #Removo o preço do produto
                            for item in precos_limpos:
                                arquivo = open(nome_arquivo_2, 'a')
                                arquivo.write(f'{precos_limpos[i]}\n')
                                i += 1
                                arquivo.close()

                            #Deixo o arquivo vazio para que a lista antiga não se repita
                            i = 0
                            arquivo = open(nome_arquivo, 'w')
                            arquivo.write('')
                            arquivo.close()
                            
                            #Removo o nome do produto
                            for item in produtos_limpos:
                                arquivo = open(nome_arquivo, 'a')
                                arquivo.write(f'{produtos_limpos[i]}\n')
                                i += 1
                                arquivo.close()

                            os.system("cls")
                            print(f"O Produto {produto} foi removido com sucesso!")
                            os.system("pause")
                
                    if produto.title() == "Sair":
                        break

            else:
                if opcao.title() == "Sair":
                    break
                
                else:
                    mensagem = 'Opção inválida.'
    
    else:
        if opcao.title() == "Sair":
            break
        
        else:
            mensagem = 'Opção inválida.'
