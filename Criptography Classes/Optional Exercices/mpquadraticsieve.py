import math
#Multi-polinomial quadratic sieve 

def isQuadratic(a,p):
    #para ser quadratico a^2 é igual a: a mod p
    for i in range(1,p-1):
        if (i**2)%p == a %p:
            return 1

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
    M= Bmax**2
    S=list()
    for i in range(M+1):
        S.append(m+i)
        if i != 0:
            S.insert(0,m-i)
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
    return factor_base

def function(x,n):
    return x**2-n

def polinomial(x,n,pj):
    a=pj**2
    
    b=0
    for i in range(a-1):
        if (i**2)%a == n%a:
            if 0<i<(a/2):
                b=i
    c=(b**2-n)/a

    return (a*(x**2) + 2*b*x + c)



n = 393204907393204907

Bmax = round(math.exp((1/2)*math.sqrt(math.log(n)*math.log(math.log(n)))))

B = gerarB(n,Bmax)

m=round(n**(1/2))

S=gerarS(m,Bmax)
f=[function(i,n)for i in S]

soft_factors=findSoft(S,f,B)

parity_factors={}
parity_factors_f1={}

for i in soft_factors:
    parity_factors[i]=[k%2 for k in soft_factors[i]]

print('si:fatorização de f(si)','\n',soft_factors)
print('si:paridade da fatorização de fj(si)','\n',parity_factors)

selector=round(math.sqrt(math.sqrt(2*n))/math.sqrt(Bmax**2))
print('pj deve ser um primo proximo de:',selector,'Alterar diretamente no código, pj predefinido é 3')
pj=3
f1=[polinomial(i,n,pj) for i in S]
soft_factors_f1=findSoft(S,f1,B)

for i in soft_factors_f1:
    parity_factors_f1[i]=[k%2 for k in soft_factors_f1[i]]

print('si:fatorização de fj(si)','\n',soft_factors_f1)
print('si:paridade da fatorização de fj(si)','\n',parity_factors_f1)