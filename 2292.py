#1 6 12 18
i = int (input())
# 1 7 19 37
num = 1
i-=1
while i > 0:
    i -= num*6
    num+=1
print(num)