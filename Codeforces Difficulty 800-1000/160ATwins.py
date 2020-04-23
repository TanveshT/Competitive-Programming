n = int(input())
coins = list(map(int, input().split()))

coins = sorted(coins, reverse = True)
sumOfAll = sum(coins)

sumIhave = 0
count = 0
for x in coins:
    if sumIhave > (sumOfAll - sumIhave):
        break
    else:
        sumIhave += x
        count += 1

print(count)