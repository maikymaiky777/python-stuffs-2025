scores = [45, 78, 90, 55, 88]
amount = 0
for i in range(len(scores)):
    if scores[i] >= 80:
        amount += 1
print(amount)