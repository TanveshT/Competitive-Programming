a = input()
b = input()
n = len(a)
ans = ""
for i in range(n):
    if a[i] != b[i]:
        ans += "1"
    else:
        ans += "0"
print(ans)