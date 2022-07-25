def f(x, y, m):
    #print('\nf(',x,y,m,')')
    if(m == 1):
        print(image[y][x], end='')
        return
    num = image[y][x]
    flag = False
    for i in range(0, m):
        for j in range(0,m):
            #print('\n -- ' + image[y+i][x+j] + ' ', m)
            if not (image[y+i][x+j] == num):
                #print('\n', x+i, y+i, num, image[y+i][x+j])
                print('(', end='')
                f(x, y, m//2) 
                f(x+m//2, y, m//2)
                f(x, y+m//2, m//2)
                f(x+m//2, y+m//2, m//2)
                print(')', end='')
                return
        
    print(num, end='')
    return
    
    
    return

N = int(input())
image = []
for i in range(0, N):
    kk = input()
    image.append([])
    for j in kk:
        image[i].append(j)
#print(image)
f(0,0,N)
print()
