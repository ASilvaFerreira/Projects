#McEliece cryptosystem based on a [7-4] linear code that can correct 1bit
import numpy as np 
from itertools import compress, product
from random import *
from numpy.linalg import inv

def codewords():
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

#definir o cryptosistema

#chave privada
g=np.array([[1, 0, 0, 0, 0, 1, 1],[0, 1, 0, 0, 1, 0, 1],[0, 0, 1, 0, 1, 1, 0],[0, 0, 0, 1, 1, 1, 1]])
p=np.array([[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,1,0,0,0,0,0],[0,0,0,0,0,0,1],[1,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0]])
s=np.array([[1,0,1,0],[1,1,0,1],[0,0,1,0],[0,0,0,1]])

#chave publica
chave=s.dot(g.dot(p))
#print("A chave publica é:\n", chave)

#encriptação
def encriptar(msg,key):
    #msg é do tipo string
    #key é uma matriz obtida com o numpy
    
    message = np.array([int(i) for i in msg]) #tornar a string numa lista de inteiros
    new_message=list()
    
    for i in range(7):
        new_message.append(str((message.dot(key[:,i]))%2))
    
    #introduzir um erro random
    value = randint(0,6) 

    if new_message[value] == '0':
        new_message[value] = '1' 
    else:
        new_message[value] = '0'

    new_message="".join(new_message)
    return new_message

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

def desencriptar(cipher):
    # conjunto de operações matriciais que reverte a mensagem encriptada para um estado de codigo linear
    # mensagem = inv_s * cifrada * inv_p
    # cipher entra com type str()

    cipher_l = np.array([int(i) for i in cipher])

    unpermuted = cipher_l.dot(inv(p))
    # descodificar a matriz não permutada
    # as codewords() estão em str() type
    unpermuted = [str(int(i)) for i in unpermuted]
    decoded = min_distancia(unpermuted)
    # para decifrar resta multiplicar a matriz inversa de S
    # voltar a colocar decoded em np.array
    decoded = np.array([int(i) for i in decoded])
    inverted_message=decoded[0:4]

    deciphered = inverted_message.dot(inv(s))
    deciphered = "".join([str((int(i)%2)) for i in deciphered])
    return deciphered


mensagem='1110'
mensagem_encriptada=encriptar(mensagem,chave)
print("Usando a chave publica a mensagem:",mensagem,"foi codificada e encriptada para:",mensagem_encriptada)

mensagem_recuperada=desencriptar(mensagem_encriptada)
print("Utilizando a chave privada a mensagem foi desencriptada e descodificada:", mensagem_recuperada)