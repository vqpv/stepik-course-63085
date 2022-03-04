num = list(input())

c = 0

while num:
    if int(num[0]) == 7:
        c += 1
    num.pop(0)

print(c)
