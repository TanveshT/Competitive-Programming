t = int(input())

result = []
for _ in range(t):
    
    matrix = []
    n = int(input())
    
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    
    diagSum = 0
    rowCount = 0
    columnCount = 0

    for i in range(n):
        diagSum += matrix[i][i]

    for i in range(n):
        row = [0] * (n + 1)
        for j in range(n):
            row[matrix[i][j]] += 1
            if row[matrix[i][j]] > 1:
                rowCount += 1
                break

    for j in range(n):
        row = [0] * (n + 1)
        for i in range(n):
            row[matrix[i][j]] += 1
            if row[matrix[i][j]] > 1:
                columnCount += 1
                break

    result.append([diagSum, rowCount, columnCount])

for i in range(t):
    print("Case #"+str(i+1)+":", result[i][0], result[i][1], result[i][2], sep = " ")