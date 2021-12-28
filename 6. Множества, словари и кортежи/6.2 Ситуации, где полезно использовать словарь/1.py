string = input().lower()

d = {}

for char in string:
    if char.isalpha():
        d[char] = d.get(char, 0) + 1

print(d)
