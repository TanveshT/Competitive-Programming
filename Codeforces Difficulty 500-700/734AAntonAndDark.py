n = int(input())
arr = input()
countA = 0
for x in arr:
    if x == 'A':
        countA += 1

half = n/2
if countA > half:
    print('Anton')
elif countA < half :
    print('Danik')
else:
    print('Friendship')