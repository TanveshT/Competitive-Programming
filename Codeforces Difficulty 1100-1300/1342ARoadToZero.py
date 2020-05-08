t = int(input())

for _ in range(t):

    x, y = map(int , input().split())
    a, b = map(int, input().split())
    x, y = abs(x), abs(y)
    dif = abs(x-y)
    minv = min(x,y)
    print(min(dif*a + minv*b,(x+y)*a))