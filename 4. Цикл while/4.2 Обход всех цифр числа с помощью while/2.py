num = list(input())

s = 1

while num:
    s *= int(num[0])
    num.pop(0)

print(s)
