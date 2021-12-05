for i in range(5):
    string = input().split()
    if "1" in string:
        index_1, index_2 = i, string.index("1")

print(abs(2 - int(index_1)) + abs(2 - int(index_2)))
