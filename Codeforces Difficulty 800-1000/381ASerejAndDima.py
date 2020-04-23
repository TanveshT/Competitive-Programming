n = int(input())
sTotal = 0
dTotal = 0
a = list(map(int, input().split()))
l = 0; r = n-1
add = None
for i in range(n):
    if a[l] > a[r]:
        add = a[l]
        l+=1
    else:
        add = a[r]
        r-=1
    if (i+1) % 2 == 0: dTotal += add
    else: sTotal += add

print(sTotal, dTotal, sep = " ")