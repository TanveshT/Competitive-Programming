t = int(input())

for _ in range(t):

    n, a, b = map(int, input().split())

    if a <= b/2:
        print(n*a)
    else:
        print((n//2) * b + (n%2)*a)