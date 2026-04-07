a= [1]
print("*")
for n in range(1,128):
    new = []
    for i in range(len(a)+1):
        if i == 0 or i >= len(a):
            new.append(1)
        else:
            if a[i] == a[i-1]:
                new.append(0)
            else:
                new.append(1)
    a=new
    str = ""
    for v in range(len(new)):
        if new[v] == 1:
            str = str + "*"
        else:
            str = str + " "
    print(str)