import sys
import copy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for x in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
global max
max=0

def bfs():
    global max
    q = deque()
    arr2 = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 2:
                q.append((i,j))
    visit = [ [ 0 for x in range (m)] for x in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while(1):
        if len(q)==0: break
        x,y = q.popleft()
        for i in range(4):
            if x+dx[i]>=0 and x+dx[i] <n:
                if y+dy[i] >=0  and y+dy[i] <m:
                    if arr2[x+dx[i]][y+dy[i]]==0:
                        arr2[x+dx[i]][y+dy[i]]=2
                        q.append((x+dx[i], y+dy[i]))           
    c=0
    for i in range(n):
        for j in range(m):
            if arr2[i][j]==0:
                c+=1
    if c>max:
        max=c

def wall(count):
    if count == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    wall(count+1)
                    arr[i][j] = 0


wall(0)
print(max)