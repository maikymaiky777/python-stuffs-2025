from math import ceil
import random

num = random.randint(1,9999)

for i in range(9999):
    guess = int(input())
    if guess == num:
        print("you win!!!! number: "+str(num)+" tries: " + str(i+1))
        break
    else:
        a = "higher"
        if num < guess:
            a = "lower"
        print("number is "+a)
