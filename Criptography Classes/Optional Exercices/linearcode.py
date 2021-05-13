#[7-4] linear code
# Os paramêtros que o usuário pode modificar encontram-se a partir da linha 80

from itertools import compress, product
from random import *

def encode(msg):
    lista=[int(i) for i in msg]
    
    # utilizar a matriz G para codificar
    # palavra codificada será do tipo "msg x y z"
    x=(lista[1]+lista[2]+lista[3])%2
    y=(lista[0]+lista[2]+lista[3])%2
    z=(lista[0]+lista[1]+lista[3])%2
    lista.append(x)
    lista.append(y)
    lista.append(z)
    for i in range(len(lista)):
        lista[i]=str(lista[i])
    s="".join(lista)
    return s

def codewords():
    def combinations(items):
        return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )
        # alternative:                      ...in product([0,1], repeat=len(items)) )
    def associar(conj):
        lista=list(conj)
        # ordenar a lista, caso já esteja ordenada ignora
        w=sorted(lista)
        temp = [0,0,0,0]
        for i in range(len(temp)):
            if i in w:
                temp[i]=1
        return temp
    n=[0,1,2,3]
    #lista com todas as keyword em forma de set()
    cwlist=list(combinations (n))
    words=list()

    for e in cwlist:
        words.append(encode(associar(e)))

    words=[list(word) for word in words]
    return words

def erro(mcoded):
    # introduzir um erro na palavra de código
    lista = [int(i) for i in mcoded]

    value = randint(0,6)

    if lista[value] == 0:
        lista[value] = 1 
    else:
        lista[value] = 0
    for i in range(len(lista)):
        lista[i]=str(lista[i])

    mcoded_erro = "".join(lista)
    return mcoded_erro

def min_distancia(msg):
    #verifica a distância da palavra errada com todas as palavras de código
    #msg é a mensagem codificada com um bit trocado
    lista = [i for i in msg]
    palavras=codewords()
    for palavra in palavras:
        dist = 0
        #verificar of bites diferentes 
        for k in range(len(lista)):  # distância de hamming
            if lista[k] != palavra[k]:
                dist+=1
        if dist == 1:
            original = "".join(palavra)
    return original


### Definir mensagem e uso das funções definidas para corrigir um erro aleatório na mensagem.

mensagem=input('Introduza uma mensagem de 4bits: ')
while len(mensagem) != 4:
    mensagem=input('A mensagem tem de ter apenas 4 algarismos: ') 

m_codificada=encode(mensagem) #codifica a mensagem
print("A mensagem:",mensagem,"foi codificada como:",m_codificada)
print('Após causar um erro na palavra codificada iremos tentar de novo chegar à palavra original')

for i in range(5):
    mc_errada=erro(m_codificada)
#print("A palavra de código",m_codificada,"foi alterada para:",mc_errada)

    print("A sequência errada,",mc_errada,"indica que a sequência de 7bits original é:",min_distancia(mc_errada))
# gerar um ciclo que a cada iteração altera um bit diferente

