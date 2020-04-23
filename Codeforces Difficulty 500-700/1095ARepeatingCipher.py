n = int(input())
s = input()
result = ''
i =0
j = 0
while(i<n):
    result += s[i]
    j += 1
    i += j
print(result)