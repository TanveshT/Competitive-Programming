n, h = map(int, input().split())
arr = list(map(int, input().split()))

countOfTallPeople = 0
for x in arr:
    if x > h:
        countOfTallPeople += 1

print((n-countOfTallPeople) + (countOfTallPeople * 2))