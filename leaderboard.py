lst = {
    "a":1,
    "b":2,
    "c":29,
    "d":7,
    "e":10,
}
sorted_items = dict(sorted(lst.items(), key=lambda item: item[1],reverse=True))
print("leaderboard")
i=1
for item in sorted_items:
    print(str(i)+": "+item+" ("+str(lst[item])+" power)")
    i+=1