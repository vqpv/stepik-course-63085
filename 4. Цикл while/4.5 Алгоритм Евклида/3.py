a, b = map(int, input().split())

c, d = a, b

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

if a > b:
    print((c * d) // a)
else:
    print((c * d) // b)
