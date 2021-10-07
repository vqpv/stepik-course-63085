n = int(input())

f = 0

if n % 2 == 0:
    f += round(n / 2)
else:
    f += -1 * round((n + 1) / 2)

print(f)
