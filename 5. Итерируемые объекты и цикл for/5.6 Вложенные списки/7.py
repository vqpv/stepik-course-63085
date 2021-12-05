n, m = map(int, input().split())

matrix = []
sum_s = []
sum_c = []

for _ in range(n):
    string = list(map(int, input().split()))
    matrix.append(string)
    sum_s.append(sum(string))

for j in range(m):
    sm = []
    for i in range(n):
        sm.append(matrix[i][j])
    sum_c.append(sum(sm))

print(*sum_s)
print(*sum_c)
