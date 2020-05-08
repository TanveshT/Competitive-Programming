t = int(input())

for _ in range(t):

    s, a, b, c = map(int, input().split())
    chocolates = s//c
    print(chocolates + (chocolates//a * b))