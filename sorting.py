"""sorting list elements as a string manually ignoring case but outputtimg correct case"""


"""appending lower word to word (faster)"""
string = input("enter a string\n")
s = string.split()
appendedlower = [w.lower()+w for w in s]
sortedlist = sorted(appendedlower)
final = [w[len(w)//2:] for w in sortedlist]
print(" ".join(final))

"""passing lower as key"""
# def funcMY(e):
#     return e.lower() 
    
# string = input("enter a string\n")
# s = string.split()
# s.sort(key=funcMY)
# print(" ".join(s))

