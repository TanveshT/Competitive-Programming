n, m, z = map(int, input().split())

k = m
count = 0
i = n

while(i <= z):
    if i==k:
        count+=1
    if k<i: k+=m
    elif i<k: i+=n
    else:
        k+=m
        i+=n
print(count)