n = int(input())

matrix = []

for _ in range(n):
    matrix.append(input().split())

for i in reversed(range(n)):
    string = []
    for j in reversed(range(n)):
        string.append(matrix[j][i])
    print(*string)
