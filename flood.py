sx,sy = str.split(input("size: "))
#sx,sy = 4,3
sx = int(sx)
sy = int(sy)

lst = []
data = []
ex,ey = 0,0
#ex,ey = 3,2

for i in range(sy):
    a = str.split(input())
    #a = ["1"]
    b = []
    c = []
    for j in a:
        if j.isdigit():
            b.append(int(j))
            c.append(999999999999999)
        else:
            if j == "S":
                c.append(0)
            if j =="E":
                c.append(999999999999999)
                ex,ey = j,i
                b.append(0)
            else:
                b.append(j)
            
    lst.append(b)
    data.append(c)

#lst = [["S",3,0,2],[1,5,2,4],[2,0,3,0]]
#data = [[0,999999999999999,999999999999999,999999999999999],[999999999999999,999999999999999,999999999999999,999999999999999],[999999999999999,999999999999999,999999999999999,999999999999999]]

print(lst,data)
x,y = 0,0
def func(xx,yy):
    print(x,y)
    if xx >= 0 and xx < sx and yy >= 0 and yy < sy:
        n=lst[yy][xx]
        if isinstance(n,int):
            c = n+data[y][x]
            if data[yy][xx] > c:
                data[yy][xx] = c
            print(x,y,xx,yy,n,c)
for l in range(100):
    x,y = 0 ,0
    for i in data:
        for v in i:
            if v >= 0:
                for j in range(-1,2,2):
                    xx=j+x
                    func(xx,y)
                for k in range(-1,2,2):
                    yy=k+y
                    func(x,yy)
            x+=1
        x=0
        y+=1
for i in data:
    print(i)
#print("minimum energy:",data[ey][ex])