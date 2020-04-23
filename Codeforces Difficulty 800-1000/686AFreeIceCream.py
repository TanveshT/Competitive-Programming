n, x = map(int, input().split())
distressed = 0
for _ in range(n):

    op, d = input().split()
    d = int(d)
    if op == '-' and x < d:
        distressed += 1
    elif op == '+':
        x += d
    else:
        x = max(0, x-d)

print(x, distressed, sep = " ")
    