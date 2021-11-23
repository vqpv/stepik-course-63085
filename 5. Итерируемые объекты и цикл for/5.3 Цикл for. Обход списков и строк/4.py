word = input().lower()

c = 1

for char in word:
    if word.count(char) > c:
        c = word.count(char)

print(c)
