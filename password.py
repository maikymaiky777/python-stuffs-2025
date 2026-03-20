clue = input("clue: ")
uppercase = ""
num = ""
for i in range(len(clue)):
    letter = clue[i]
    if letter.isupper():
        uppercase = uppercase + letter
    if letter.isdigit():
        num = num + letter
print("answer:", uppercase+num)