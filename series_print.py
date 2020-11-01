#Given a natural number n (where 1≤n≤9), find the sum of the series having n number of numbers such that the series is n,nn,nnn,…nnn…n times.
n = int(input())
total = 0
for i in range(n):
    val = str(n)*(i+1)
    total = total + int(val)
print(total)
