num = input()

while num[0] != '1' and int(num) < 1000000000:
    num = str(int(num[0]) * int(num))

print(num)
