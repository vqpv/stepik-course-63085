n, m = map(int, input().split())

num = 0 

for i in range(n):
    string = []
    for _ in range(m):
        string.append(num)
        num += 1
    if i % 2 == 0:
        print(*string)
    else:
        print(*reversed(string))
