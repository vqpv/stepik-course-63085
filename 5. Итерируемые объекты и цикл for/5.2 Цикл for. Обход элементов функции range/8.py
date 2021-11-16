n = int(input())

for i in range(1, n + 1):
    word = input().lower()
    if "рок" in word:
        print(i, word.find("рок") + 1, sep=' ')
