n = int(input())

i = 0
f = 0

while f < n:
    f = 2 ** i
    i += 1

if f == n:
    print(i - 1)
else:
    print("НЕТ")
