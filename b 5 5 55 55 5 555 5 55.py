amount = int(input())
nums = str.split(input())
sum = 0
avg = 0
med = 0
max = 0
min = 9999999999
alert = 0
sorted = []
for i in range(amount):
    n = float(nums[i])
    sum += n
    if n > max:
        max = n
    if n < min:
        min = n
    if n >= 37.0:
        alert += 1
    sorted.append(n)

avg = sum / amount

sorted.sort()
string = ""
for i in range(amount):
    n = float(sorted[i])
    if i == 0:
        string += format(n,".2f")
    else:
        string += (" " + format(n,".2f"))
if len(sorted) % 2 == 0:
    med = (sorted[int(len(sorted)/2-1)] + sorted[int(len(sorted)/2)]) / 2
else:
    med = sorted[int((len(sorted)-1)/2)]
print("SUM="+format(sum,".2f"))
print("AVG="+format(avg,".2f"))
print("MEDIAN="+format(med,".2f"))
print("MAX="+format(max,".2f"))
print("MIN="+format(min,".2f"))
print("ALERT="+str(alert))
print("SORTED="+string)
