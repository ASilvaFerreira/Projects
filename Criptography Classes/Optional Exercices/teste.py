n=23456788765
pj=11
a=pj**2
for i in range(a-1):
    print((i**2)%a,',',n%a)
    if (i**2)%a == n%a:
        if 0<i<(a/2):
            print('aqui')
            b=i