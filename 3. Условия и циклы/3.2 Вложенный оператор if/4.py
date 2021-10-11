a, b, c = map(int, input().split())

max_n = 0
min_n = 0

if a > b:
    if a > c:
        max_n = a
    else:
        max_n = c
    if b < c:
        min_n = b
    else:
        min_n = c
else:
    if b > c:
        max_n = b
    else:
        max_n = c
    if a < c:
        min_n = a
    else:
        min_n = c

print(max_n - min_n)
