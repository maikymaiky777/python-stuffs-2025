lst = {
    "a":[10,"Water",25,30],
    "b":[12,"Fire",40,40],
}
sorted = dict(sorted(lst.items(), key=lambda item: item[1],reverse=True))
i=1
highest = ""
total = 0
for item in sorted:
    total += lst[item][0]
    if i == 1:
        highest = item
    print(str(i)+": "+item+" (level "+str(lst[item][0])+", type: "+str(lst[item][1])+", hp: "+str(lst[item][2])+"/"+str(lst[item][3])+")")
    i+=1

print("highest level:",highest,"level", lst[highest][0])
print("average level:", total/len(lst))