"""You are given three inputs: a string, one letter, and a second letter.

Check if every instance of the first letter occurs before every instance of the second letter."""

statement,a,j=input().split(",")
a = a[2]
j = j[2]
val = statement.index(j)
if a in statement[val:]:
    print("False")
else:
    print("True")