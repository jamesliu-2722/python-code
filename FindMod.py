
# import sys

d={}

def findMod(n):
    if n in d:
        # d1 = {n, d[n]}
        d[n]=d[n]+1
    else:
        d[n]=1
    max = 0
    for n in d:
        if max < d[n]:
            max = d[n]
            mode = n
    return mode


# while(True):
x = int(input("Enter a number: "))
print (findMod(x))
s = [3,8,5,7,3]
s.sort()
print (s)

