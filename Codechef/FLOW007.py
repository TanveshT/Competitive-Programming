t = int(input())
result = []
for _ in range(t):
    s= input()
    result.append(s[::-1])

for x in result:
    print(int(x))