# RSA cryptosystem

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

alfabeto=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dic={}
for i in range(len(alfabeto)):
    dic[alfabeto[i]]=i
key_list = list(dic.keys()) 
val_list = list(dic.values())

m='CARMICHAEL'

i=len(m)-1
temp=[]
for k in m:
    temp.append(val_list[key_list.index(k)]*(27**i))
    i-=1
base27=sum(temp)
print(base27)


#cipher
q=2*(11**175)+1
r=488881
n=q*r
e=65537
d=modInverse(e,(q-1)*(r-1))
print(d)
c=pow(base27,e,n)


deciphered=pow(c,d,n)
print(deciphered)