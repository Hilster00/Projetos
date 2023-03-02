import os
import random
import time
#from winreg import QueryInfoKey
from random import choice

def criar_matriz():
    matriz=[]

    #tratamento de erro da quantidade de cidades
    while True:
        try:
            quantidade_cidades=int(input("Defina a quantidade de cidades:"))
            if(quantidade_cidades<=0):
                quantidade_cidades=int("str")
            break
        except:
            os.system("cls")
            print("Digite um valor válido")

    
    #matriz compara distancias entre cidades, representada pela linha e coluna
    #laco de repeticao das linhas
    for i in range (0, quantidade_cidades):
        
        vetor_interno=[]

        #laco de repeticao das colunas
        for j in range (0, quantidade_cidades):
            
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


def forca_bruta(matriz):
    caminho=[]
    distancias=[]

    quantidade_cidades=len(matriz)
    lista_cidades=[]


    #sorteia umma cidade para começar
    nome_cidade=random.randint(0,quantidade_cidades)  
        
    #fatorail
    fatorial=1
    for x in range(1,quantidade_cidades+1):
        fatorial*=x

    lista_cidades=[]
    for i in range(0,quantidade_cidades):
        lista_cidades.append(i)
  
    lista=lista_cidades
    while True:
        temporario=[]
       
        while True:
            cidade=choice(lista)
            if(cidade not in temporario):
                temporario.append(cidade)       
            
            
            if(len(temporario)==quantidade_cidades):                
                break
        if(temporario not in caminho):
            caminho.append(temporario)
        if(len(caminho)==fatorial):
            break   
        lista=lista_cidades
    for x in range(0,fatorial):
        distancias.append([])     
    for x in range(0,fatorial):
        distancias[x]=0
        for i in range(0, quantidade_cidades-1):
            distancias[x]+=matriz[caminho[x][i]][caminho[x][i+1]]
    menor_caminho=0

    for i in range(0,fatorial):
        if(distancias[menor_caminho]>distancias[i]):
            menor_caminho=i
    print(distancias[menor_caminho]) 
    print(caminho[menor_caminho])

os.system("cls")
beguin=time.time()
print(forca_bruta(criar_matriz()))
print("%s segundos"%(time.time()-beguin))
