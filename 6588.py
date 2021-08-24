#1000000
import sys
sosu = [1 for x in range(0, 1000000)]
sosu[1]=0
for i in range(2, 500000):
    if sosu[i]==0:
        continue
    for j in range (i*2, 1000000, i):
        if j>=1000000:
            break
        sosu[j]=0
n = int(sys.stdin.readline())

while n!=0:
    flag=False
    for i in range (3, int(n/2)+1, 2):
        if sosu[i]==1 and sosu[n-i]==1:
            flag=True
            print(n,'=',i,'+', n-i)
            break
    if not flag:
        print("Goldbach's conjecture is wrong.")
    n=int(sys.stdin.readline())
    