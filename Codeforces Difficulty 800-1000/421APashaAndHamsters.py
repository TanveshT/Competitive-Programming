n, a, b = map(int, input().split())
arthur = list(map(int, input().split()))
alex = list(map(int,input().split()))

x = [0] * (n+1)

for i in arthur:
    x[i] = 1

for i in alex:
    x[i] = 2

for i in range(1,n+1):
    print(x[i], end = " ")