""" For a given integer output list of prime factors"""

#returns a list of prime numbers in given range
def get_primes(n):
    prime_vals= []
    for i in range(2,n+1):
        isPrime = True
        for j in range(2,i):
            if i%j==0:
                isPrime = False
                break
        if isPrime: prime_vals.append(i)
    return prime_vals

num = int(input("Enter a positive integer"))
primes = get_primes(num//2) #getting prime numbers in half the range of the input number
factors = []

#finding factors
while num!=1:
    if primes: #will end up false incase of prime number input
        val = primes[0]
    else:
        factors.append(num)
        break
    if num % val == 0:
        factors.append(val)
        num = num/val
    else:
        primes.remove(val)

print(factors)



