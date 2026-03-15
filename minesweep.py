sizeX, sizeY = str.split(input())
mines = int(input())
sizeX = int(sizeX)
sizeY = int(sizeY)
stuff = [
    [-1,-1],[0,-1],[1,-1],
    [-1,0],        [1,0],
    [-1,1],[0,1],[1,1],
]
data = []
for x in range(sizeX):
    data2 = []
    for y in range(sizeY):
        data2.append(0)
    data.append(data2)
for m in range(mines):
    x,y = str.split(input())
    x = int(x)
    y = int(y)
    data[x][y] = "x"
for x in range(sizeX):
    for y in range(sizeY):
        n = data[x][y]
        if n == 0:
            bombs = 0
            for t in range(len(stuff)):
                tile = stuff[t]
                tileX = tile[0] + x
                tileY = tile[1] + y
                if tileX >= 0 and tileX < sizeX:
                    if tileY >= 0 and tileY < sizeY:
                        if data[tileX][tileY] == "x":
                            bombs+=1
            data[x][y] = bombs
                

for x in range(sizeX):
    string = ""
    for y in range(sizeY):
        n = data[x][y]
        if y == 0:
            string = string + str(n)
        else:
            string = string + " " + str(n)
    print(string)