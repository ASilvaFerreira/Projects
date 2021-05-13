import sys
import math
import re
import numpy as np
from sympy import sieve
from sympy import Mul, Pow
from sympy.ntheory import legendre_symbol, factorint,isprime


def calculodeparametros(n):
	m=math.floor(math.sqrt(n))
	B0=math.floor(math.exp((1/2)*math.sqrt(math.log(n)*math.log(math.log(n)))))
	primos=[i for i in sieve.primerange(3, B0)]
	B=[-1,2]
	b=([legendre_symbol(16843009, i) for i in primos])
	count=0
	for i in b:
		if i==1:
			B.append(primos[count])
		count+=1
	M=B0**2
	numerossuaves=len(B)+1
	S=range(m-M,m+M+1)
	
	return S,B


def ObterFactorização(S,n,B):
	f=[]
	for s in S:
		fs=s**2-n
		f.append(fs)
	fatorizados=[]
	for si in f:
		fat=factorint(si)
		fatorizados.append(fat)
	produtos=[]
	fatmax=[]
	Bsuave=[]
	UmPrimoGrande=[]
	DoisPrimoGrande=[]
	count=0
	siump=[]
	sidoisps=[]
	for i in fatorizados:
		produto=1
		NumGrandesprimos=0
		for key in i:
			produto *= key**i[key]
		produtos.append(produto)
		for a in list(i.keys()):
			if list(i.keys())[-1]==-1:
				if list(i.keys())[-2]>=B[-1]**2:
					continue
				elif a>B[-1] and a<=B[-1]**2:
					NumGrandesprimos+=1
			else:
				if list(i.keys())[-1]>=B[-1]**2:
					continue
				elif a>B[-1] and a<=B[-1]**2:
					NumGrandesprimos+=1
		if NumGrandesprimos==1:
			UmPrimoGrande.append(i)
			siump.append(S[count])
		if NumGrandesprimos==2:
			if list(i.keys())[-1]==-1:
				if list(i.keys())[-2]*list(i.keys())[-3]>B[-1]**2 and list(i.keys())[-2]*list(i.keys())[-3]<=B[-1]**3:
						DoisPrimoGrande.append(i)
						sidoisps.append(S[count])
			else:
				if list(i.keys())[-1]*list(i.keys())[-2]>B[-1]**2 and list(i.keys())[-1]*list(i.keys())[-2]<=B[-1]**3:
					DoisPrimoGrande.append(i)
					sidoisps.append(S[count])
		if produto==f[count] and list(i.keys())[-1]!=-1 and list(i.keys())[-1]<=B[-1]:
			Bsuave.append(i)
		elif produto==f[count] and list(i.keys())[-1]==-1 and list(i.keys())[-2]<=B[-1]:
			Bsuave.append(i)
		count+=1
	return sidoisps,siump,fatorizados,DoisPrimoGrande,UmPrimoGrande,Bsuave

def relações(sidoisps,siump,fatorizados,DoisPrimoGrande,UmPrimoGrande,Bsuave,n):
	#print(DoisPrimoGrande)
	for i in range(len(UmPrimoGrande)):
		umprimo=[]
		um=UmPrimoGrande[i]
		if list(um.keys())[-1]==-1:
			umprimo.append(list(um.keys())[-2])
		else:
			umprimo.append(list(um.keys())[-1])
		#print(umprimo,'tu')
		for j in range(i+1,len(UmPrimoGrande)):
			doisprimo=[]
			dois=UmPrimoGrande[j]
			if list(dois.keys())[-1]==-1:
				doisprimo.append(list(dois.keys())[-2])
			else:
				doisprimo.append(list(dois.keys())[-1])
			#print(doisprimo,'eu')
			count=0
			for h in DoisPrimoGrande:
				doisprimos=[]
				if list(h.keys())[-1]==-1:
					doisprimos.append(list(h.keys())[-3])
					doisprimos.append(list(h.keys())[-2])
				else:
					doisprimos.append(list(h.keys())[-2])
					doisprimos.append(list(h.keys())[-1])
				#print(doisprimos)
				if doisprimos[0]==umprimo[0] and doisprimos[1]==doisprimo[0]:
					vetornulo={}
					expoentes={}
					for a in um:
						if a not in vetornulo:
							vetornulo[a]=um[a]%2
							expoentes[a]=um[a]
						vetornulo[a]=vetornulo[a]%2
					for b in dois:
						if b not in vetornulo:
							vetornulo[b]=dois[b]%2
							expoentes[b]=dois[b]
						else:
							vetornulo[b]+=dois[b]%2
							expoentes[b]+=dois[b]
						vetornulo[b]=vetornulo[b]%2
					for c in h:
						if c not in vetornulo:
							vetornulo[c]=h[c]%2
							expoentes[c]=h[c]
						else:
							vetornulo[c]+=h[c]%2
							vetornulo[c]=vetornulo[c]%2
							expoentes[c]+=h[c]

					#print(expoentes,vetornulo,a)
					vetorzero=[]
					for v in vetornulo:
						vetorzero.append(vetornulo[v])
					if any(vetorzero)==False:
						print(vetornulo,expoentes)
						y=1
						for exp in expoentes:
							y*=exp**(expoentes[exp]/2)
						y=y%n
						x=(siump[i]*siump[j]*sidoisps[count])%n
						n1=(x-int(y))%n
						n2=(x+int(y))%n
						primeirofactor=math.gcd(n1,n)
						segundofactor=math.gcd(n2,n)
						print(x,y,siump[i],siump[j],sidoisps[count])
						if primeirofactor==1 or segundofactor==1:
							continue
						return primeirofactor,segundofactor				
					else:
						continue
					
						
						#print(siump[i],siump[j],sidoisps[count])
				count+=1
					#print(UmPrimoGrande[i],UmPrimoGrande[j],'ele',h)
	
	#print(umprimo,doisprimo,primos)





def main(n):
	S,B=calculodeparametros(n)
	sidoisps,siump,fatorizados,DoisPrimoGrande,UmPrimoGrande,Bsuave=ObterFactorização(S,n,B)
	primeirofactor,segundofactor=relações(sidoisps,siump,fatorizados,DoisPrimoGrande,UmPrimoGrande,Bsuave,n)
	print(primeirofactor,segundofactor)
	#print(factorint(3239),factorint(242925))
main(393204907)
#print(math.exp((1/2)*math.sqrt(math.log(16843009)*math.log(math.log(16843009)))))