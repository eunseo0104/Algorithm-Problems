str = input()
l = len(str)
a=-2
cnt =0
while a!=-1:
    a=str.find('c=', a+2)
    cnt+=1
cnt-=1
a=-2
while a!=-1:
    a=str.find('c-', a+2)
    cnt+=1
cnt-=1
a=-2
while a!=-1:
    a=str.find('dz=', a+2)
    cnt+=1
cnt-=1
a=-2
while a!=-1:
    a=str.find('d-', a+2)
    cnt+=1
cnt-=1
a=-2
while a!=-1:
    a=str.find('lj', a+2)
    cnt+=1
cnt-=1
a=-2
while a!=-1:
    a=str.find('nj', a+2)
    cnt+=1
cnt-=1
a=-2
while a!=-1:
    a=str.find('s=', a+2)
    cnt+=1
cnt-=1
a=-2
while a!=-1:
    a=str.find('z=', a+2)
    cnt+=1
cnt-=1

print(l-cnt)
