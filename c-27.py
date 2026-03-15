sizeX, sizeY = str.split(input())
sizeX = int(sizeX)
sizeY = int(sizeY)
data = []
for x in range(sizeX):
    data.append(str.split(input()))
for x in range(sizeX):
    for y in range(sizeY):
        n = data[sizeX-x-1][y]
        if n == "*" and x != 0:
            data[sizeX-x][y] = "*"


for x in range(sizeX):
    string = ""
    for y in range(sizeY):
        n = data[x][y]
        if y == 0:
            string = string + str(n)
        else:
            string = string + " " + str(n)
    print(string)