a, b, c = map(int, input().split())
largestSide = max(a,b,c)
print(max(largestSide - (a + b + c - 1 - largestSide), 0))
