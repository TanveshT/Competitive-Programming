t = int(input())

for _ in range(t):

    a = input()
    b = input()
    c = input()

    flag = True
    n = len(c)

    for i in range(n):
        if c[i] != a[i] and c[i] != b[i]:
            flag = False
            break
    
    if flag:
        print('YES')
    else:
        print('NO')