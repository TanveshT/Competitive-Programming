n, c = map(int,input().split())
a = list(map(int, input().split()))

words = 1
wordsLost = 0
for i in range(1,n):
    if a[i] - a[i-1] > c:
        wordsLost += words
        words = 1
    else:
        words += 1

print(words)
