n = int(input())
x = list(map(int, input().split()))

x = sorted(x)
count = 0
for i in range(1,n):
    if x[i] - x[i-1] != 1:
        count += (x[i] - x[i-1] - 1) 

print(count)