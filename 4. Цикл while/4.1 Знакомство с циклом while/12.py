a, b = map(int, input().split())

s = 0
h = 0

while a > 0:
    h += 1
    a -= 1
    s += 1
    if b == s:
        a += 1
        s = 0

print(h)
