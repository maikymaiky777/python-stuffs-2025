grid = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 0],
[1, 2, 3, 4, 5],
[2, 4, 6, 8, 0],
[3, 6, 9, 2, 5]
]

num = 2
xx=0
yy=0
total = 0
for x in grid:
    print()
    for y in x:
        if y == num:
            grid[xx][yy] = "*" + str(num) + "*"
            total += 1
        yy+=1
    xx+=1
    yy=0
print(num, "found", total, "times!")
for x in grid:
    print(x)