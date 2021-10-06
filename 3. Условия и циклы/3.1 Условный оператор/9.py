k1, k2 = input(), input()

if (ord(k1[0]) + ord(k1[1])) % 2 == (ord(k2[0]) + ord(k2[1])) % 2:
    print('YES')
else:
    print('NO')
