num = int(input())

simple_nums = 0

for i in range(num + 1, num * 2):
    count = 0
    if i % 2 != 0:
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            simple_nums += 1

print(simple_nums)
