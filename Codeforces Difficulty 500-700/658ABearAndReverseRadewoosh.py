n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))

scoreLimak = 0
scoreRadewoosh = 0
time1 = 0
time2 = 0

for i in range(n):

    time1 += t[i]
    time2 += t[n-(i+1)]
    scoreLimak += max(0, (p[i] - (c * time1)))
    scoreRadewoosh += max(0, (p[n-(i+1)] - (c * time2)))


if scoreLimak > scoreRadewoosh:
    print('Limak')
elif scoreRadewoosh > scoreLimak:
    print('Radewoosh')
else:
    print('Tie')