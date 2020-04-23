stones = {'purple':['Power',0],
'green': ['Time',0],
'blue': ['Space',0],
'orange': ['Soul',0],
'red': ['Reality',0],
'yellow': ['Mind',0]}

count = 0

n = int(input())
for _ in range(n):
    stones[input()][1] += 1

res = []
for x in stones:
    if stones[x][1] == 0:
        count += 1
        res.append(stones[x][0])

print(count)
for x in res:
    print(x)