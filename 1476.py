e, s, m = input().split()
e=int(e)
s=int(s)
m=int(m)
sum = 0
while True:
    mm=min(e,s,m)
    sum = sum+ mm
    e=e-mm
    s=s-mm
    m=m-mm
    if e==0 and s ==0 and m ==0:
        break
    if e==0:
        e=15
    if s==0:
        s=28
    if m==0:
        m=19
print(sum)