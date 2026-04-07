c = 0
for i in range(4445):
    if i % 14 == 12 and i % 16 == 14 and i % 18 == 16:
        c += 1
        print(i, "correct")
    else:
        print(i, "wrong")
print("ans:",c)