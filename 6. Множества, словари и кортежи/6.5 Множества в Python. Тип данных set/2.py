a, b = set(map(int, input().split())), set(map(int, input().split()))

print(*sorted(a - b))
