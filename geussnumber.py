import random


while True:
    num1 = random.randint(-10,30)
    num2 = random.randint(-10,30)
    type = "+"
    c = num1 + num2
    if random.randint(1,3) == 1:
        type = "x"
        num1 = round(num1/2)
        num2 = round(num2/2)
        c = num1 * num2
    elif random.randint(1,2) == 1:
        type = "-"
        c = num1 - num2
    
    q = "What is " + str(num1) + " " + type + " " + str(num2)
    
    print(q)
    ans = input("input ans: ")
    if int(ans) == c:
        print("✅")
    else:
        print("❌")
    