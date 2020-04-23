a, b, c = map(int, input().split())
ans = 0
print(2*c+min(a,b)+min(max(a,b),min(a,b)+1))