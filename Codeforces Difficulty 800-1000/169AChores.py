n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h = sorted(h)

print(h[b] - h[b-1])