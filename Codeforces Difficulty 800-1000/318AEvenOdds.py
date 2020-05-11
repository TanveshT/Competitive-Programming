n, k = map(int, input().split())
half = (n+1) // 2
if  k > half:
    print(2+((k-half-1)*2))
else:
    print(1+((k-1)*2))