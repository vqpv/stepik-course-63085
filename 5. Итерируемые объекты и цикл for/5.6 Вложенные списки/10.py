n, m = map(int, input().split())

line = 0
column = 0
maximum = 0
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            line = i
            column = j

print(maximum)
print(line, column)
