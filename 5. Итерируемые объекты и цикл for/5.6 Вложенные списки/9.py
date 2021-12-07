n, m = map(int, input().split())

ss = []

for _ in range(n):
    string = map(int, input().split())
    ss.append(sum(string))

print(max(ss))
print(ss.index(max(ss)))
