num = input()

num = num.rjust(6, '0')

print('YES' if sum(map(int, num[:3])) == sum(map(int, num[3:])) else 'NO')
