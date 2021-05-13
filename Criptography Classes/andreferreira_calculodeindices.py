from sympy import *
from random import *
from numpy import *


def discretelog(g,b,p): # g^x = b mod p

    def primes(x):
        n=x

        lower = 1
        upper = n

        prime=list()
        for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime.append(num)
        return prime

    def lfactors(numero,Base):
        # B é a base de fatores
        factors=[]
        for i in Base:
            while numero%i == 0:
                factors.append(i)
                numero = numero/i
        return factors

    def isSoft(num,BF):
        r=1
        num_factors=lfactors(num,BF)
        if len(num_factors)==0:
                return 'Not Soft'
        else:
            for k in num_factors:
                r=r*k
            testnumber = r
            if testnumber==num:
                return 'Soft'


    def relations(BF):
        #escolher numeros Z random entre 1 e p-1
        GZfactors={}
        t=0
        while t==0:
            for i in range(len(BF)):
                c=0
                while c==0:
                    z=randint(1,p-1)
                    N=pow(g,z,p)
                    if isSoft(N,BF)=='Soft':
                        if z not in GZfactors: 
                            tempvector=lfactors(N,BF)
                            newvector=[0]*len(BF)
                            for k in BF:
                                for s in tempvector:
                                    if s == k:
                                        newvector[BF.index(k)]=newvector[BF.index(k)]+1
                            GZfactors[z]=newvector
                        c=1
            if gcd(int(round(linalg.det(array([GZfactors[i] for i in GZfactors])))),(p-1)) ==1:
                return GZfactors
                t=1
            else:
                GZfactors={}

    def solveforxbase(dicti):

        a = Matrix([dicti[i] for i in dicti])
        inv=a.inv_mod((p-1))
        b= Matrix(list(dicti.keys()))
        x=(inv*b)%(p-1)
        X=[i for i in x]
        return X

    def solvefory(b,g,p,BF):
        c=0
        while c==0:
            y=randint(1,p-1)
            temp=pow(g,y,p)
            aux1=(b*temp)%p

            if isSoft(aux1,BF) == 'Soft':
                soft=aux1
                c=1
        soft_factors=lfactors(soft,BF)
        newvector=[0]*len(BF)
        for k in BF:
            for s in soft_factors:
                if s == k:
                    newvector[BF.index(k)]=newvector[BF.index(k)]+1
        return y, newvector

    def findsolution(xbase,y,relacoes):
        temp=0
        for i in range(len(relacoes)):
            temp+=xbase[i]*relacoes[i]

        x=int((temp-y)%(p-1))
        return x

    Bmax=30
    BF = primes(Bmax)
    print('A base de fatores utilizada contem,',len(BF),'elementos:',BF)
    relationvectors=relations(BF)
    print('\nObtiveram-se aleatóriamente 10 vetores de fatores primos, correspondentes a numeros B-suaves g^z:','\n',relationvectors)
    xbase = solveforxbase(relationvectors)
    print('\nA resolução deste sistema dá-nos os valores de cada xi nesta base de fatores:','\n',xbase)

    print('\nNa segunda fase calcula-se b*g^y mod p , com y aleatório, de modo a este numero ser B-suave')

    y,relacoes=solvefory(b,g,p,BF)
    print('Neste caso y=',y,'produz um valor B-suave cuja fatorização pode ser descrita pelo vetor:',relacoes)
    x=findsolution(xbase,y,relacoes)
    return x

p=nextprime(3*10**7)

g=primitive_root(p)

b=80252

x=discretelog(g,b,p)

print('\nPara este caso, o valor de x é:',x)

print(pow(g,x,p),'é igual a',b)