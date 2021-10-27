n, k = map(int, input().split())

i = 1
t = 5 * i

while t <= 240 - k and i <= n:
    t += i * 5
    i += 1

print(i - 1)
