import math
n = int(input())

if n%2 == 0:
    print(n//2)
else:
    print(-1*(math.ceil(n/2)))