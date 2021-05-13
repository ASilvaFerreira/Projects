#for primality tests
def primes():
    n=10000

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



