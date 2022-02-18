n = int(input())

list_c = [1, 5, 10, 20, 100]
summa = 0

for i in reversed(list_c):
    summa += n // i
    n %= i

print(summa)
