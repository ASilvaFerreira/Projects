q=2*(11**175)+1
print(q)
n=100000
'''
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
print(prime)


lista=list()
for i in prime:
    print(i)
    if ((q-1)/i)%i == 0:
        lista.append(i)
print()

conta=pow(5,q-1,q)
print(conta)
'''

g=int((q-1)/87491)
print(pow(5,g,q))