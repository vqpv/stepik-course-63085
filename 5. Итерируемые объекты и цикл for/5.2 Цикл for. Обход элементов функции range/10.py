n = int(input())

s = 0

for i in range(3, n):
    if (i % 3 == 0) or (i % 5 == 0):
        s += i

print(s)
