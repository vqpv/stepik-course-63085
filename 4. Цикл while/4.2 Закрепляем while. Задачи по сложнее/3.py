n = int(input())

c, s = 0, 0

while True:
    i = int(input())
    if n >= s + i:
        s += i
        c += 1
    else:
        break

print('Довольно!')
print(s)
print(c)
