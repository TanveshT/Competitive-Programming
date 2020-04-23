t = int(input())
result = []

for _ in range(t):

    a, b, x, y = map(int, input().split())
    x += 1; y+= 1
    areaArr = [(a-x)*b, a*(b-y), (x-1)*b, a*(y-1)]
    result.append(max(areaArr)) 

for x in result:
    print(x)