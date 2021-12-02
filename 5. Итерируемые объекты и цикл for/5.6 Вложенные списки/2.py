n = int(input())

matrix = []

for _ in range(n):
    matrix.append(input().split())

for i in range(n):
    string = []
    for j in range(n):
        string.append(matrix[j][i])
    print(*string)
