import random

real=0
total=0

lst = []
sort=[]
for i in range(100):
    num = random.randint(0,100)
    lst.append(num)
    sort.append(num)
    if num > 0:
        real += 1
    total+=num
sort.sort(reverse=True)
top10=[]
avg=total/len(lst)
for i in range(10):
    top10.append(sort[i])
print(real, "real coins")
print("average:",avg)
print("total:",total)
print("top 10:",top10)