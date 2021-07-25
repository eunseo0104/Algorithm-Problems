import math
i = 0
a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
d=0
if b>=c:
    print(-1)
    exit(0)
print( math.floor(a/(c-b)+1))