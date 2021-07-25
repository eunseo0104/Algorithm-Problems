num = int(input())
str = []
for i in range(num):
    str.append(input())

count = 0
s = '' 
for i in range(num):
    s=''
    for j in range(len(str[i])-1):
        s+=str[i][j]
        if str[i][j] == str[i][j+1]:
            continue

        if s.find(str[i][j+1])!=-1:
            count+=1
            break
print(num-count)
        