import random

hp = 150
go = True
g=0
while go:
    r = random.randint(1,50)
    d = random.randint(1,4)
    a = input("goblin coming, castle health: "+ str(hp)+ " continue? y/n ")
    if a == "n":
        go = False
        print("score:",g*10)
        break
    print("goblin power:",r, "defense bonus",d )
    hp -= r-d
    g+=1
    if hp <= 0:
        print("game over")
        break