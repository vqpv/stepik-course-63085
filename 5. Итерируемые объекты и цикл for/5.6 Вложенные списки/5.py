n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(input().split())

for i in reversed(range(n)):
    string = []
    for j in range(m):
        string.append(matrix[i][j])
    print(*string)
