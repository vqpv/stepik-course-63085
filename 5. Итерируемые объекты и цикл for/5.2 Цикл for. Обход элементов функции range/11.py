n = int(input())

for _ in range(n):
    word = input()
    l_w = len(word)
    if l_w > 10:
        print(word[0] + str(l_w - 2) + word[-1])
    else:
        print(word)
