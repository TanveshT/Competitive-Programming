n = int(input())
a =  list(map(int,  input().split()))
x = []

for i in range(n):
    x.append([a[i],i])

x = sorted(x, key = lambda x: x[0])

for i in range(n//2):
    print(x[i][1]+1,x[n-i-1][1]+1, sep = " ")