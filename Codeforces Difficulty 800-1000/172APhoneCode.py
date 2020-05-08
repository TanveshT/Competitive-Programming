n = int(input())
phones = []
for i in range(n):
    phones.append(input())

m = len(phones[0])
 
count = 0
flag = False
for j in range(m):
    compare = phones[0][j]
    for i in range(n):
        if compare != phones[i][j]:
            flag = True

    if flag:
        break
    else:
        count+=1

print(count)