n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

aSolved = 0
bSolved = 0
dissimilar = 0

for i in range(n):
    if a[i] == 1 and a[i] != b[i]:
        aSolved += 1
    if b[i] == 1 and a[i] != b[i]:
        bSolved += 1

if aSolved == 0:
    print(-1)
else:
    print((bSolved+1)//aSolved)
