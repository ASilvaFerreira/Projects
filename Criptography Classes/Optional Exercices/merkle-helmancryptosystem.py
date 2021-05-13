#merkle-helman cryptosystem
import random as r
import math 

def modInverse(a, m) : 
	m0 = m 
	y = 0
	x = 1

	if (m == 1) : 
		return 0

	while (a > 1) : 

		# q is quotient 
		q = a // m 

		t = m 

		# m is remainder now, process 
		# same as Euclid's algo 
		m = a % m 
		a = t 
		t = y 

		# Update x and y 
		y = x - q * y 
		x = t 


	# Make x positive 
	if (x < 0) : 
		x = x + m0 

	return x 

def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
 

def isPrime(n): 
      
    # Corner cases  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
      
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if(n % 2 == 0 or n % 3 == 0): 
        return False
      
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
      
    return True
  
# Function to return the smallest  
# prime number greater than N  
def nextPrime(N): 
  
    # Base case  
    if (N <= 1): 
        return 2
  
    prime = N 
    found = False
  
    # Loop continuously until isPrime returns  
    # True for a number greater than n  
    while(not found): 
        prime = prime + 1
  
        if(isPrime(prime) == True): 
            found = True
  
    return prime 


#gerar sequencia supercrescente
def superincreasing(first,number):
    #first is the first ellement
    #number is the number of elements
    c=0
    seq=list()
    a=first
    while c<number:
        a=sum(seq)+r.randint(2,100)
        seq.append(a)
        c+=1
    return seq


def privatekey():
    sseq=superincreasing(7,11)
    p=nextPrime(sum(sseq)+r.randint(2,10))
    a=r.randint(0,p)

    while computeGCD(a,p)!=1:
        a=r.randint(0,p)

    b=modInverse(a,p)
    #criar a sequência que é a chave publica
    public=list()

    for i in sseq:
        public.append((a*i)%p)
    return public,sseq,p,a,b

def toBinary(texto):
    alfabeto='*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic={}
    for i in range(len(alfabeto)):
        dic[alfabeto[i]]=i
    key_list = list(dic.keys()) 
    val_list = list(dic.values())

    base10=val_list[key_list.index(texto[0])]*27+val_list[key_list.index(texto[1])]
    return '{0:011b}'.format(base10)


def cifrar(pkey,epsilons):

    c=sum([int(epsilons[i])*pkey[i] for i in range(len(pkey))])
    return c

public_key,private_seq,p,a,b=privatekey()

message='RI'



epsilons=toBinary(message)
cifrado=cifrar(public_key,epsilons)

print(message,'foi cifrado como:',cifrado)

def solveKnapsack(c,sequencia,b,p):
    w=(c*b)%p
    eps=list()
    print(w)
    print(sequencia)
    
    while w!=0:
        if sequencia[-1]<w:
            w=w-sequencia[-1]
            sequencia.pop(-1)
            eps.append(1)
        else:
            sequencia.pop(-1)
            eps.append(0)

solveKnapsack(cifrado,private_seq,b,p)