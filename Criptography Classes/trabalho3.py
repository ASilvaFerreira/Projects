import sys
import math
import re
import numpy as np
import sympy
from sympy import sieve
from sympy import Mul, Pow, nextprime
from sympy.ntheory import legendre_symbol, factorint,isprime
from sympy.ntheory.residue_ntheory import primitive_root
from numpy.linalg import inv
import random
from sympy import Matrix, pprint



def descobrirpg(n): 
	p=nextprime(n) #p já é primo, através do teorema de lucas é possível verificar isso
	#print(p)
	g=primitive_root(p) #raiz primitiva mais pequena de p 
	#print(g)
	return p,g

def dictovetor(FB): #dicionario com os primos da base de factores
	dictvetor={}
	for j in FB:
		if j not in dictvetor:
			dictvetor[j]=0
	return dictvetor

def obtervetorbsuave(vetorfactorizado,dictvetor1): # obter os vetores B-suave
	vetor=[]
	for a in vetorfactorizado:
		dictvetor1[a]+=vetorfactorizado[a]
	for b in dictvetor1:
		vetor.append(dictvetor1[b])
	return vetor


def verificardependencia(vetorBsuave,relationss,e): #verificação da independencia das relações
	relationss[e]=vetorBsuave
	#print(relationss,'eu')
	matrix=np.array(relationss)
	_, inds = sympy.Matrix(matrix).T.rref()
	#lambdas, V =  np.linalg.eig(matrix.T)
	# The linearly dependent row vectors 
	#print (matrix[lambdas == 0,:])
	#lambdas, V =  np.linalg.eigvals(matrix.T)
	#print(lambdas)
	return inds



def descobrirb(p,g): # para obter as relações e os valores de k
	B=30 # valor máximo para a base de fatores
	FB=[i for i in sieve.primerange(2, B)]
	relations=[]
	nrelation=len(FB)
	for j in range(nrelation):
		nulovetor=[]
		for i in range(nrelation):
			nulovetor.append(0)
		relations.append(nulovetor)
	nrelation=0
	valordek=[]
	e=0
	inds=[]
	# tenho de gerar o k aleatoriamente e garantir que nao se repete
	relations=np.zeros((len(FB),len(FB)), dtype = int)
	determinante=np.linalg.det(np.array(relations))
	while len(inds)<=len(FB) and math.gcd(int(round(determinante)),(p-1))!=1:
		k=random.randint(1, p-1)%(p-1)
		if e==10:
			e=0
			relations=np.zeros((len(FB),len(FB)), dtype = int)
			valordek=[]
		if k in valordek:
			continue
		dictvetor1=dictovetor(FB)
		factor=pow(g,k,p)
		vetorfactorizado=factorint(factor)
		if list(vetorfactorizado.keys())[-1]>=B:
			continue
		else:
			vetorBsuave=obtervetorbsuave(vetorfactorizado,dictvetor1)
			#print(vetorfactorizado)
			#print(vetorBsuave)
			#verificar se é independente
			if e==0:
				relations[e]=vetorBsuave
				valordek.append(k)
				determinante=np.linalg.det(np.array(relations))
				#print(vetorfactorizado,k)
				e+=1
			else:
				inds=verificardependencia(vetorBsuave,relations,e)
				if len(inds)-1!=e:
					e=e
				else:
					relations[e]=vetorBsuave
					e+=1
					nrelation+=1
					valordek.append(k)
					determinante=np.linalg.det(np.array(relations))
		#print(vetorfactorizado,k,relations,e,determinante,inds)
	return relations,valordek,FB,B

						

			#matrix=np.array([vetorBsuave])

			#vetorBsuave.append(k)

def descobrirx(relations,valordek,p,FB): #valores de cada x da base de factores
	print(relations)
	a = Matrix(relations)
	print(a)
	print('tipo é',type(a))
	v=a.inv_mod((p-1)) #calulo a inversa
	b = Matrix(valordek)
	valoresdex=v*b%(p-1)
	valordecadax={}
	for i in range(len(valoresdex)):
		if 'x'+str(FB[i]) not in valordecadax:
			valordecadax['x'+str(FB[i])]=valoresdex[i]
	return valordecadax


def segundafase(valordecadax,n,p,g,B): #calcular o valor de x para 3**x=79835 mod p
	Bsuave=[]
	while len(Bsuave)==0:
		y=random.randint(1, p-1)%(p-1)
		valorparafatorizar=(n*g**y)%p
		factorização=factorint(valorparafatorizar)
		if list(factorização.keys())[-1]>=B:
			continue
		else:
			Bsuave.append(factorização)
	#print(Bsuave,y)
	x=0
	for i in Bsuave:
		for j in i:
			x+=i[j]*valordecadax['x'+str(j)]
	x-=y
	x=x%(p-1)
	return Bsuave,y,x	






def main(n):
	p,g=descobrirpg(n)
	print("valor de p = {} \n valor de g = {}".format(p,g))
	relations,valordek,FB,B=descobrirb(p,g)
	print('relações = {} \n valores de k = {}'.format(relations,valordek))
	valordecadax=descobrirx(relations,valordek,p,FB)
	print("valores de cada x da base de fatores = {}".format(valordecadax))
	Bsuave,y,x=segundafase(valordecadax,n,p,g,B)
	print('y = {} \t x = {} \n Bsuave = {}'.format(y,x,Bsuave))
	print(pow(g,int(x),p))

main(79835)