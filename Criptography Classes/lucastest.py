#lucas test

n=3*10**7+1

print(n)




for i in range(14,n-1):
    if pow(i,n-1,n) == 1:
        a=i
        break

print(a,'demonstrates that a^(n-1)=1 mod n:', pow(a,n-1,n))


firstq=int((n-1)/5)
print(firstq)
print(pow(a,firstq,n))