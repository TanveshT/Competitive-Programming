n = int(input())
a = [0] + list(map(int, input().split()))

flag = False
for i in range(1,n+1):
    if a[a[a[i]]] == i:
        flag = True
        break

if flag:
    print('YES')
else:
    print('NO')