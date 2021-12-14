n, m = map(int, input().split())

matrix = []
point = '.'
count = 0


for _ in range(n):
    matrix.append(point + input() + point)

matrix.insert(0, point * (m + 2))
matrix.append(point * (m + 2))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (matrix[i][j] == point) and (matrix[i][j] == matrix[i - 1][j] == matrix[i][j - 1] == matrix[i][j + 1] == matrix[i + 1][j]):
            count += 1

print(count)
