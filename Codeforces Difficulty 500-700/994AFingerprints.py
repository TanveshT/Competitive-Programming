n, m = map(int, input().split())
sequence = list(map(int, input().split()))
fingerprints = list(map(int, input().split()))

res = []
for x in sequence:
    if x in fingerprints:
        res.append(x)

for x in res:
    print(x, end = " ")