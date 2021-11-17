n = int(input())

strings = []

for _ in range(n):
    string = input().lower()
    if "соль" not in string:
        strings.append(string)

print(*strings, sep=', ')
