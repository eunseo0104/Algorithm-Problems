import sys
goal = int(sys.stdin.readline())
n = int(sys.stdin.readline())
if n!=0: arr = set(sys.stdin.readline().split())
else: arr = set()
make=0
i=0
minimum=abs(goal-100)
#만들수있는 조합 중 차가 가장 작은 수 찾기
for i in range(1000001):
    for j in str(i):
        if j in arr:
            break
    else:
        temp = min(minimum, abs(goal-i)+len(str(i)))
        if minimum>temp:
            minimum=temp
            make=i

print(minimum)