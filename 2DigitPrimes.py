def sieve(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p] == True:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, num + 1):
        if prime[p]:
            print(p)

num = 99
print("These are the prime numbers with 2 or less digits")
sieve(num)