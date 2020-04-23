n, m = map(int, input().split())
s = input().split()
t = input().split()
q = int(input())

resultList = []
for _ in range(q):
    k = int(input())
    resultList.append(s[k%n - 1] + t[k%m - 1])

for x in resultList:
    print(x)
