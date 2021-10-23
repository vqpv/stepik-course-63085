n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = sorted(list(map(int, input().split())))

c, s = 0, 0

while s < min(n,m):
    if abs(a[s] - b[s]) <= 1:
        c += 1
    s += 1

print(c)
