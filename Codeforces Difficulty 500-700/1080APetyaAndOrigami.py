from math import ceil

n, k = map(int, input().split())

print(ceil(n*8/k) + ceil(n*5/k) + ceil(n*2/k))