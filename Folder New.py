m = input("membership Y/N: ")

items = int(input("items: "))
list = []
for i in range(items):
    list.append(float(input("item "+str(i+1)+": ")))
total = round(sum(list)*100)/100
if m == "Y":
    
    print(round(total*0.95*100+0.5)/100)
else:
    if total >= 500:
        print(round(total*0.97*100+0.5)/100)
    else:
        print(round(total*100)/100)