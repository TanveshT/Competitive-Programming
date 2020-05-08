x, y, z = map(int, input().split())
g, p, b = map(int, input().split())

if g >= x and (g+p-x) >= y and ((g+p+b)-(x+y)) >= z:
    print('YES')
else:
    print('NO')