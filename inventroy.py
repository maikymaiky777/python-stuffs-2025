from ast import Pass


treasure = {
    "gold": [{"name": "Gold Coins", "value": 10, "quantity": 50}],
    "gems": [{"name": "Ruby", "value": 100, "quantity": 5}],
    "weapons": [{"name": "Dragon Sword", "value": 500, "quantity": 1}]
}

def calcValue():
    value = 0
    for item in treasure:
        data = treasure[item][0]
        amount = data["value"] * data["quantity"]
        value += amount

        print(item, amount)
    print("Value: " + str(value))

def findhighest():
    mostvalue = 0
    mostvalueitem = ""
    for item in treasure:
        data = treasure[item][0]
        amount = data["value"] * data["quantity"]
        if amount > mostvalue:
            mostvalue = amount
            mostvalueitem = item

        print(item, amount)
    print("Most Valuable: " + mostvalueitem + " (" + str(mostvalue) + ")")

def display():
    for item in treasure:
        data = treasure[item][0]
        print(item + " value: " + str(data["value"]) + " quantity: " + str(data["quantity"]))

def addnew(name, value, quantity):
    treasure[name] = [{"name": name, "value": int(value), "quantity": int(quantity)}]

while True:
    cmd = input("command: (calculate,findhighest,display,insert)")
    if cmd == "calculate":
        calcValue()
    elif cmd == "findhighest":
        findhighest()
    elif cmd == "display":
        display()
    elif cmd == "insert":
        n,v,q = str.split(input("name, value, quantity: "))
        addnew(n,v,q)