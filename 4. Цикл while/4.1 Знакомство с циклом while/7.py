X, Y = map(int, input().split())

c = 1

while X <= Y:
    X *= 1.15
    c += 1

print(c)
