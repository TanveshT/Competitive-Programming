t = int(input())

result = []
for _ in range(t):

    result.append(input().strip('0').count('0'))

for x in result:
    print(x)