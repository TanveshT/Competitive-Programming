s = input()
arr = set()
for x in s:
    if x not in ['}','{',',',' ']:
        arr.add(x)
print(len(arr))