import os
import random
import time
from random import choice

def criar_matriz():
    matriz=[]

    #tratamento de erro da quantidade de cidades
    while True:
        try:
            quantidade_cidades=int(input("Defina a quantidade de cidades:"))
            if(quantidade_cidades<=0):
                print("Digite um valor maior que 0")
                continue
            break
        except:
            os.system("cls")
            print("Digite um valor válido")

    
    #matriz compara distancias entre cidades, representada pela linha e coluna
    #laco de repeticao das linhas
    for i in range(quantidade_cidades):
        
        vetor_interno=[]

        #laco de repeticao das colunas
        for j in range(quantidade_cidades):
            
            #distancia da cidade com ela mesma
            if(i == j):
                distancia=0

            #distancia cadastrada anteriormente
            elif(j<i):
                distancia=matriz[j][i]

            #nova distancia
            else:
               #distancia definida por sorteio
               distancia=random.randint(1,900)
            
            vetor_interno.append(distancia)
        matriz.append(vetor_interno)

    return matriz

def caminho_heuristica(matriz):
    caminho=[]
   
    quantidade_cidades=len(matriz)
    lista_cidades=list(range(quantidade_cidades)

    #sorteia uma cidade para comecar
    nome_cidade=random.randint(0,quantidade_cidades)

    #laco para  execultar enquanto nao tiver passado por todas cidades
    for vez in range(quantidade_cidades):
        
        #adiciona a cidade atual a lista de cidades percorridas
        caminho.append(nome_cidade)
        
        #remove da lista de cidades a cidade atual
        lista_cidades.remove(nome_cidade)

        #distancia infinita para sempre ter uma menor
        menor_distancia=float("inf")

        #nome da cidade que tambem sera usada na linha
        i=nome_cidade

        #laco de coluna com base na lista de cidades
        for j in lista_cidades:

            #compara se a distancia e menor
            if(matriz[i][j]<menor_distancia ):
            
                #distancia menor atualiza as variaveis para a proxima compacao
                menor_distancia=matriz[i][j]
                nome_cidade=j
        
    return caminho

os.system("cls")
beguin=time.time()
print(caminho_heuristica(criar_matriz()))
print("%s segundos"%(time.time()-beguin))
