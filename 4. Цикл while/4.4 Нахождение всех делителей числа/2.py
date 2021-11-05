num = int(input())

n = num
summa = 0

while n > 0:
    if num % n == 0:
        summa += n
    n -= 1

print(summa)
