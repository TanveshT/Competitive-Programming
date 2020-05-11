t = int(input())
 
for _ in range(t):
 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    a = sorted(a)
    b = sorted(b)
 
    if (a[0] + b[0]) == a[1] and a[1] == b[1] :
        print('YES')
    else:
        print('NO')
