n = int(input())

print(tuple(i for i in range(n, n * n + 1) if i % 2 == 1))
