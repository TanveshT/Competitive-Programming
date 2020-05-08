n, k = map(int, input().split())
a = list(map(int , input().split()))
thres = a[k-1]
count = 0
for x in a:
    if x >= thres and x != 0:
        count += 1

print(count)