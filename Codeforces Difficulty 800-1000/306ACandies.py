import math

n, m = map(int, input().split())
div = n/m
ans = [math.floor(div)] * (m-n%m)
ans += [math.ceil(div)] * (n%m)


print(*ans, sep = " ")