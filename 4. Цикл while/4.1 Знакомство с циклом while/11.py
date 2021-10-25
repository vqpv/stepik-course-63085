n, m = map(int, input().split())

a, b, c = 0, 0, 0

while a * 2 < n:
    if a + (n - a ** 2) ** 2 == m:
        c += 1
    a += 1
        
print(c)
