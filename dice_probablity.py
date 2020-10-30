import random
def rolldice(*args):
    total=0
    for arg in args:
        total +=arg
    lister = [0]*(total)
    for _ in range(10):
        val = random.randint(len(args),total)
        print(val)
        lister[val-1]+=1
    print(lister)

print("Enter the values")
vals= list(map(int,input().split()))
rolldice(*vals)
