inv = []
def add(name,amount):
    curr = 0
    if inv[name]:
        curr = inv[name]
    inv[name] = amount+curr
    print(inv)
while True:
    a,b = str.split(input())
    add(a,b)