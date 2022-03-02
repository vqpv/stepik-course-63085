n, t = map(int, input().split())

i = 1

while (t < 60 * 4) and (i <= n):
    i += 1
    t += 5 * i

print(i - 1)
