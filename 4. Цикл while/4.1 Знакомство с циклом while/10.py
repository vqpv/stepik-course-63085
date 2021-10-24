h = int(input())

i, c = 1, 1

while h > 0:
    i += 1
    c += i
    h -= c

print(i - 1)
