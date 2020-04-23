n = int(input())

result = []
for _ in range(n):

    s = input().split('_')
    s = s[::-1][0]
    if 'po' in s[-2:]: result.append('FILIPINO')
    elif 'desu' in s[-4:] or 'masu' in s[-4:]: result.append('JAPANESE')
    else: result.append('KOREAN')

for x in result:
    print(x)