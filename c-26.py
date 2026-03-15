sizeX, sizeY = str.split(input())
sizeX = int(sizeX)
sizeY = int(sizeY)
data = []
data2 = []
data3 = []
def calc(a,b):
    if a == "-" and b == "-":
        return "-"
    elif a == "+" and b == "-":
        return "+"
    elif a == "-" and b == "x":
        return "x"
    elif a == "+" and b == "x":
        return "*"
    elif a == "-" and b == "+":
        return "+"
    elif a == "x" and b == "-":
        return "x"
    elif a == "x" and b == "+":
        return "*"
    return False
for x in range(sizeX):
    data.append(list(input()))
for x in range(sizeX):
    data2.append(list(input()))
for x in range(sizeX):
    data3.append([])
    for y in range(sizeY):
        data3[x].append("")
for x in range(sizeX):
    for y in range(sizeY):
        n = data[x][y]
        n2 = data2[x][y]
        data3[x][y] = calc(n,n2)
        
for x in range(sizeX):
    string = ""
    for y in range(sizeY):
        n = data3[x][y]
        if y == 0:
            string = string + str(n)
        else:
            string = string + str(n)
    print(string)