#10000
sel = [0 for x in range(0, 10001)]
for i in range(1, 10000):
    sum = i
    while not(i == 0) :
        sum+=i%10
        i=int(i/10)
    if sum<=10000: sel[sum]=1

for i in range(1,10001):
    if sel[i] == 0:
        print(i)