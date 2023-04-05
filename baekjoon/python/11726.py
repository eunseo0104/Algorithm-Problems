import sys
arr = [0 for x in range(0,1001)]
sys.setrecursionlimit(10**8)
def f(x):
    if arr[x]!=0:
        return arr[x]
    if x==0: 
        return 1
    elif x<0: 
        return 0
    arr[x] = (f(x-1) + f(x-2)) % 10007
    return arr[x]


i = int(input())
print(f(i))