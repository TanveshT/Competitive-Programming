n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

count = 0
mid = ((n+1)//2) - 1
for i in range(n):
    count += matrix[i][i]
    matrix[i][i] = 0
    count += matrix[i][n-(i+1)]
    matrix[i][n-(i+1)] = 0

for i in range(n):
    count += matrix[mid][i]
    matrix[mid][i] = 0

for i in range(n):
    count += matrix[i][mid]
    matrix[mid][i] = 0


print(count)