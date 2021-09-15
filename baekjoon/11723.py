import sys
#4673 keep
n = int(sys.stdin.readline())


S = []
for i in range(0,n):
    str = sys.stdin.readline()
    if str == 'all\n':
        S=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif str == 'empty\n':
        S=[]
    else:
        str, i = str.split()
        i = int(i)
    
    if str == 'add':
        if i not in S:
            S.append(i)
    elif str == 'remove':
        if i in S:
            S.remove(i)
    elif str == 'check':
        print(int(i in S))
    elif str == 'toggle':
        if i in S:
            S.remove(i)
        else:
            S.append(i)
    
