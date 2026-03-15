amount = input()
a = str.split(input())
end = []
for i in range(len(a)):
    n = float(a[i])
    no = True
    for b in range(len(end)):
        h = end[b]
        if h[0] == n:
            no = False
    if no:
        end.append([n,a.count(a[i])])
high = 0
ans = 0
for i in range(len(end)):
    n = end[i]
    if n[1] > high:
        high = n[1]
        ans = n[0]
print(ans)
