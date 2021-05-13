# Iterative Python 3 program to find 
# modular inverse using extended 
# Euclid algorithm 

# Returns modulo inverse of a with 
# respect to m using extended Euclid 
# Algorithm Assumption: a and m are 
# coprimes, i.e., gcd(a, m) = 1 
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


# Driver program to test above function 
a = 65537
m = (2*(11**175))*488880
print("Modular multiplicative inverse is", 
	modInverse(a, m)) 

q=2*(11**175)
r=488880
modInverse(65537,q*r)