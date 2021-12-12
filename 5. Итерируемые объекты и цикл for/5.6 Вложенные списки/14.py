n, m = map(int, input().split())

matrix_1 = []
matrix_2 = []
errors = 0

for _ in range(n):
    matrix_1.append(input())

input()

for _ in range(n):
    matrix_2.append(input())

for i in range(n):
    for j in range(m):
        if matrix_1[i][j] == matrix_2[i][j]:
            errors += 1

print(errors)
