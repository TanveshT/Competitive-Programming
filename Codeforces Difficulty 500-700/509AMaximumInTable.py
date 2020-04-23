n = int(input())
matrix = [[1] * n]
for i in range(1,n):
    row = []
    for j in range(n):
        if j == 0: row.append(1)
        else: row.append(matrix[i-1][j] + row[j-1])
    matrix.append(row)
print(matrix[n-1][n-1])