import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
arr={}
for i in range(0, n):
    arr[i]=list(map(int, input().split()))
global answer
answer = 0
k=[[-1 for y in range(501)] for x in range(0, 501)]
def f(i, j):
    global answer
    if i==0 and j==0: 
        answer +=1
        return 1

    if k[i][j]!=-1:
        return k[i][j]
        
    a=0
    if i+1<n: 
        if arr[i][j] < arr[i+1][j]: a += f(i+1, j)
    if j+1<m:
        if arr[i][j] < arr[i][j+1]: a += f(i, j+1)
    if i-1>=0: 
        if arr[i][j] < arr[i-1][j]: a += f(i-1, j)
    if j-1>=0: 
        if arr[i][j] < arr[i][j-1]: a += f(i, j-1)
    k[i][j] = a

    return k[i][j]
    

print(f(n-1,m-1))