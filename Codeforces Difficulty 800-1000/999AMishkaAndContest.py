n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0
l,r = 0, n-1

while(l<=r):
    if a[l] <= k or a[r] <= k:
        count += 1
        if a[l] <= k: l+=1
        elif a[r] <= k: r-=1
    else:
        break

print(count)