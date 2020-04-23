n = int(input())
count = 0
for x in [5, 4, 3, 2, 1]:
    count += n//x
    n = n%x
print(count)