n = int(input())
result = []

for _ in range(n):

    s = input()
    length = len(s)

    if length > 10:
        result.append(s[0] + str(length-2) + s[length-1])
    else:
        result.append(s)

for x in result:
    print(x)