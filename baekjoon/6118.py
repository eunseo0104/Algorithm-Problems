import sys
from collections import deque

i = list(map(int, sys.stdin.readline().split()))
n = i[0]
m = i[1]
graph = [ [] for x in range (0, n+1)]

for j in range(m):
    i = list(map(int, sys.stdin.readline().split()))
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

dist = [-1 for x in range(n+1)]
q = deque()
q.append([1,0])
dist[1]=0
while q:
    temp = q.popleft()
    for i in graph[temp[0]]:
        if dist[i] == -1:
            q.append([i, temp[1]+1])
            dist[i]=temp[1]+1

ma = 0
count=1
index=0
for i in range(1, n+1):
    if dist[i]==-1:
        continue
    if ma < dist[i]:
        ma = dist[i]
        count=1
        index = i
    elif ma == dist[i]:
        count = count+1

print(index, ma, count)