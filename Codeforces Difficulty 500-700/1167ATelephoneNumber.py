t = int(input())

res = []
for _ in range(t):

    n = int(input())

    count = 0
    s = input()

    for x in s:
        if x == '8':
            break
        else:
            count += 1

    if n - count >= 11:
        res.append('YES')
    else:
        res.append('NO')

for x in res:
    print(x)