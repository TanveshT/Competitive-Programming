n, k = map(int, input().split())
a = list(map(int, input().split()))
p = [0] * (101)

for i in range(n):
    p[a[i]] = i+1

count = 0
answer = []
for i in range(1,101):
    if p[i] > 0:
        answer.append(p[i])
        count += 1

if count >= k:
    print('YES')
    for i in range(k):
        print(answer[i], end = " ")
else:
    print('NO')