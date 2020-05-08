t = int(input())

for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    add = sum(a)
    print((add+n-1)//n)