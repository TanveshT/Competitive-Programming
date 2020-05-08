n = int(input())
a = list(map(int, input().split()))

x = [[0,0]] * (1001)

for i in range(n):
    x[a[i]] = [i, a[i]]
    
answer = []
for i in range(1,1001):
    if x[i][1] > 0:
        answer.append(x[i])
answer = sorted(answer, key = lambda x: x[0])

print(len(answer))
for x in answer:
    print(x[1], end = " ")