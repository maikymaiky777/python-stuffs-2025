classes = int(input())
minutes = int(input())

total = classes * minutes
hours = total // 60
mins = total % 60
hs = "hour"
ms = "minute"
if hours > 1:
    hs = "hours"
if minutes > 1:
    ms = "minutes"
if total == 0:
    print("No teaching")
elif mins == 0.0:
    print(str(hours) + " hours")
elif hours == 0.0:
    print(str(mins) + " minutes")
else:
    print(str(hours) + " hours " + str(mins) + " minutes")