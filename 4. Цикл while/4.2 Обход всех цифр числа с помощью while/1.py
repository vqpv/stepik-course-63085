num = list(input())

s = 0

while num:
    s += int(num[0])
    num.pop(0)

print(s)
