import sys
n = int(sys.stdin.readline())
i=0
l=1
for j in range(n):
    i=i+j+1
    if i>=n:
        front=l-i+n
        if l%2==0:
            print(str(front)+'/'+str(l+1-front))
        else:
            print(str(l+1-front)+'/'+str(front))
        break
    l=l+1

