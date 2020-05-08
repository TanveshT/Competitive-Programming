n = int(input())
a = list(map(int, input().split()))
x = sorted(enumerate(a), key = lambda y:y[1])
print(x[n-1][0]+1, x[n-2][1])