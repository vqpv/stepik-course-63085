n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

if (n_1 + n_2 > n_3) and (n_1 + n_3 > n_2) and (n_2 + n_3 > n_1):
    print('YES')
else:
    print('NO')
