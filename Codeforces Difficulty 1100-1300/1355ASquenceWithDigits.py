t = int(input())

for _ in range(t):

    n, k = map(int, input().split())

    while(k>1):
        x = str(n)
        add = int(min(x))*int(max(x))
        if add == 0: break
        n += add
        k-=1

    print(n)
