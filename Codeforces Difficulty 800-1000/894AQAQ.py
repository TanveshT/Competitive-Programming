s = input()
n = len(s)

count = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if s[i] == 'Q' and s[j] == 'A' and s[k] == 'Q':
                count += 1

print(count)