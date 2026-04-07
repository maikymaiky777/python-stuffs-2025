sizeX,sizeY=60,16
w = 2
s = 2
c = 0
cc = 0
lst2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lst3 = ["-","-"]
for i in range(sizeX-2):
    if c < w and cc < len(lst2):
        lst3.append(lst2[cc])
    else:
        lst3.append("-")
        cc+=1
    c+=1
    c = c % (w+1)
lst = []
for y in range(sizeY):
    n = []
    for x in range(sizeX):
        if y == sizeY-1:
            n.append("*")
        else:
            a=sizeY-y-1
            if x == 0:
                n.append(f"{a:02d}")
            elif lst3[x] != "-" and a <= lst3[x]:
                n.append("⪏")
            else:
                n.append(" ")
        
    lst.append(n)
#⪏⩩⫻
for i in lst:
    n = ""
    for b in i:
        n=n+b
    print(n)