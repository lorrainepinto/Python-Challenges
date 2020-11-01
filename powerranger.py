#Given 3 inputs n, minimum, & maximum, find the number of values raised to the nth power that lie in the range [minimum, maximum], inclusive.
import math
root,mini,maxi=input().split(",")
root,mini,maxi=int(root),int(mini),int(maxi)
v1 = mini**(1/root)
v2 = maxi**(1/root)
v1 = math.ceil(v1)
v2 = math.floor(v2)
total = 0
for i in range(v1,v2+1):
    if i**root >= mini and i**root <=maxi :
        total = total + 1
print(total)