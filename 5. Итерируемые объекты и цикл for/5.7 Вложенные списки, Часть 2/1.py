n = int(input())

matrix = []
count = 0

for _ in range(n):
    matrix.append(input().split())

for i in range(n):
    for j in range(n):
        if matrix[i][0] == matrix[j][1]:
            count += 1

print(count)
