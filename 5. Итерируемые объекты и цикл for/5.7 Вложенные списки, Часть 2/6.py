n, m = map(int, input().split())

matrix = []
s = []
c = []

for i in range(n):
    string_1 = input()
    matrix.append(string_1)
    if 'S' not in string_1:
        s.append(i)

for j in range(m):
    string_2 = []
    for ii in range(n):
        string_2.append(matrix[ii][j])
    if 'S' not in string_2:
        c.append(j)

l_s = len(s)
l_c = len(c)

print((l_s * m) + (l_c * n) - (l_s * l_c))
