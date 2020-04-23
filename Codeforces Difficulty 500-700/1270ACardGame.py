t = int(input())

result = []
for _ in range(t):

    n, k1, k2 = map(int, input().split())

    player1Cards = list(map(int, input().split()))
    player2Cards = list(map(int, input().split()))

    player1Max = max(player1Cards)
    player2Max = max(player2Cards)

    if player1Max > player2Max:
        result.append("YES")
    else:
        result.append("NO")

for x in result:
    print(x)