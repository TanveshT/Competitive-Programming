n = int(input())

result = ''
if n%2 == 0:
    result += ' '.join(['2'] * (n//2))
else:
    result += ' '.join(['2'] * ((n-2)//2))
    result += ' 3'
    
print(n//2)
print(result)