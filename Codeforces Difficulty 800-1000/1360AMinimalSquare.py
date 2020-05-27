import math

t = int(input())

for _ in range(t):

    a, b = map(int, input().split())

    print(min(max(2*a,b), max(a, 2*b))**2)