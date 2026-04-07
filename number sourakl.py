sizeX,sizeY=15,15
lst = []
for x in range(sizeX):
    n = []
    for y in range(sizeY):
        n.append(" ")
    lst.append(n)

a = 2
dirs = [[1,0],[0,1],[-1,0],[0,-1]]
cur = 0
sx,sy = (sizeX-1)//2,(sizeY-1)//2
b = True

while b:
    for i in range(1,a+1):
        print(a,cur,dirs[cur],b,i)
        x,y = sx,sy
        d = dirs[cur]
        x += d[0]*i
        y += d[1]*i
        if i == a:
            sx,sy = x,y
        if x < 0 or x >= sizeX or y < 0 or y >= sizeY:
            b = False
            break
        lst[x][y] = "*"
    
    cur = (cur + 1) % 4
    if cur % 2 == 0:
        a += 2
    



for i in lst:
    n = ""
    for b in i:
        n=n+b
    print(n)