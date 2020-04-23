n = int(input())
s = input()

count = 0
for i in range(n):

    if int(s[i])%2 == 0:
        count += (i+1)

print(count)