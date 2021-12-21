x, y = map(int, input().split())

if x < y:
    print([i ** 2 for i in range(x, y + 1)])
else:
    x, y = y, x
    print([i ** 3 for i in reversed(range(x, y + 1))])
