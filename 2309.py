
def f(ki):
        for i in range(0, 8):
            for j in range(i+1, 9):
                if ki[i]+ki[j]==s:
                    ki.remove(ki[j])
                    ki.remove(ki[i])
                    return ki
ki=[0]*9
for i in range(0,9):
    ki[i]=int(input())
s = sum(ki)
s = s-100
ki.sort()
ki = f(ki)
for i in ki:
    print(i)
