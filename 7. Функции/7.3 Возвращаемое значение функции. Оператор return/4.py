def first_unique_char(string):
    for char in string:
        if string.count(char) == 1:
            first_char = string.index(char)
            break
        else:
            first_char = -1
    return first_char
