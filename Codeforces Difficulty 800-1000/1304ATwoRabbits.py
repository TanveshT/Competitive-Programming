t = int(input())

for _ in range(t):

    x, y, a, b = map(int, input().split())

    gap = y-x

    if gap%(a+b) != 0 or gap == a == b == 1:
        print(-1)
    else:
        print(gap//(a+b))