""" print hill or valley or niether based on input
 example: if 1 2 4 2 then hill
        if 4 3 2 3  then valley
        if 1 3 4 5 or 4 3 2 1 then neither """
vals = list(map(int, input().split()))
try:
    if vals[1]>vals[0]:
        test = vals.index(max(vals))
        if vals[test]>vals[test+1]:
            print("Hill")
        else:
            print("neither")
    else:
        test = vals.index(min(vals))
        if vals[test]<vals[test+1]:
            print("Valley")
        else:
            print("neither")
except:
    print("neither")
