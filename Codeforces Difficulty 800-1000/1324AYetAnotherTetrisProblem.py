t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    x = [i%2 == 0 for i in a]

    flag = True

    for i in range(1,n):
        if x[i] != x[i-1]:
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')