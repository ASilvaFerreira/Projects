import math
#Quadratic sieve

def isQuadratic(a,p):
    #para ser quadratico a^2 é igual a: a mod p
    for i in range(1,p-1):
        if (i**2)%p == a %p:
            return 1

def function(x):
    n=16843009
    return x**2-n
#for primality tests

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

def gerarB(n,Bmax):
    B=[2]
    p=primes(Bmax)
    for i in p:
        if isQuadratic(n,i)==1:
            B.append(i)
    print('Base de fatores Gerada:',B)  
    return B

# Encontrar factores pequenos
def lfactors(numero,Base):
    # B é a base de fatores
    factors=[]
    if numero < 0:
        factors.append(-1)
        numero = numero*(-1)

    for i in Base:
        while numero%i == 0:
            factors.append(i)
            numero = numero/i
    return factors

def gerarS(m,Bmax):
    M=Bmax**2
    print('A gerar S, aguarde até',M)
    S=list()
    for i in range(M+1):
        S.append(m+i)
        if i != 0:
            S.insert(0,m-i)
    print('Conjunto S foi gerado, com diametro:',2*M)
    return S

def findSoft(S,F,B):
    # checks if a  number is B-soft
    teste=list()
    soft={}
    for i in F:
        teste.append(lfactors(i,B))
    
    #calculate the numbers given by the factors
    number=list()
    for l in teste:
        r=1
        if len(l)==0:
            number.append('Not soft')
        else:
            for k in l:
                r=r*k
            number.append(r)
    for i in range(len(number)):
        if number[i]==F[i]:
            soft[S[i]]=teste[i]
    #return soft
    factor_base={}
    for i in soft:
        factor_base[i]=[0]*len(B)
        for k in B:
            for s in soft[i]:
                if s == k:
                    factor_base[i][B.index(k)]=factor_base[i][B.index(k)]+1
    print('B-suaves, terminado')
    return factor_base
            

#n = 1684300921234567843234
n = 393204907
Bmax = round(math.exp((1/2)*math.sqrt(math.log(n)*math.log(math.log(n)))))*4
print('Bmax é:',Bmax)
B = gerarB(n,Bmax)

m=round(n**(1/2))
print('Valor central de S:',m)

S=gerarS(m,Bmax)
print('A calcular f(si)')
f=[function(i)for i in S]
print('f(si) calculados, a procurar B-Suaves')

soft_factors=findSoft(S,f,B)

parity_factors={}

for i in soft_factors:
    parity_factors[i]=[k%2 for k in soft_factors[i]]

print('B-Suaves:',soft_factors)
print('B-suaves, vetor fatores paridade:',parity_factors)
