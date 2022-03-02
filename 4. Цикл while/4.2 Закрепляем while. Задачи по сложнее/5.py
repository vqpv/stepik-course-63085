n = int(input())

i, s = 0, 0

while s < n:
    i += 1
    s += i
    n -= s

if n < 0:
    print(i - 1)
else:
    print(i)
