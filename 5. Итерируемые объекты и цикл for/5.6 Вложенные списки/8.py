n = int(input())

matrix = []
output = "Yes"

for _ in range(n):
    matrix.append(input().split())

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            output = "No"
            break

print(output)
