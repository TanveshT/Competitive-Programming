n = int(input())
a = list(map(int, input().split()))
unattended = 0
check = 0
for x in a:
    if x < 0 and check == 0:
        unattended += 1
    elif x < 0:
        check -= 1
    else:
        check += x

print(unattended)