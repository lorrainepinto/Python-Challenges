#Given an integer  n  the number of rows in a * triangle, write a program to get the triangle with  n  rows.
n = int(input())
print(" "*(n-1)+"*")
for i in range(n-2):
    print(" "*(n-2-i)+"*"+" "*(2*i+1)+"*")
print(" "+"*"*(2*(n-3)+3))

