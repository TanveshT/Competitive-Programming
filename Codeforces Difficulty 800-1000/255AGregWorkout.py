n = int(input())
a = list(map(int, input().split()))

answer = {0: 'chest', 1:'biceps', 2:'back'}
repitation = [0, 0, 0]

for i in range(n):
    if (i+1) % 3 == 0:
        repitation[2] += a[i]
    elif (i+1) % 3 == 2:
        repitation[1] += a[i]
    else:
        repitation[0] += a[i]
maxValue = 0
index = None
for i,v in enumerate(repitation):
    if v > maxValue: maxValue = v; index = i

print(answer[index])