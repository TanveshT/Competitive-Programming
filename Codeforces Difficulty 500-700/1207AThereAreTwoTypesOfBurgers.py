t = int(input())

for _ in range(t):

    b, p, f = map(int, input().split())
    h, c = map(int, input().split())

    b = b//2

    income = 0

    if h<c:
        h, c = c, h
        p, f = f, p

    count = min(b, p)
    b -= count
    income += count * h

    count = min(b, f)
    b -= count
    income += count * c

    print(income)
