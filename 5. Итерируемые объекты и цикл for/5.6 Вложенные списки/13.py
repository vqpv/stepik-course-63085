n = 4
matrix = []
answer = "Yes"

for _ in range(n):
    matrix.append(list(input()))

for i in range(n - 1):
    for j in range(n - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            answer = "No"

print(answer)
