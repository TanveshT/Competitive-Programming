alphaDict = {'z': 0, 'e': 0, 'r': 0, 'o': 0, 'n': 0}

n = int(input())
s = input()
for x in s:
    alphaDict[x] += 1

result = [1] * min(alphaDict['o'],alphaDict['n'],alphaDict['e']) + [0] * alphaDict['z']
result = ' '.join(map(str,result))
print(result)