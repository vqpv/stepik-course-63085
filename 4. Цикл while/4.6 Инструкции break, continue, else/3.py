n = int(input())

c = 0

while n != 1:
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n // 2
    c += 1
    
print(c)
