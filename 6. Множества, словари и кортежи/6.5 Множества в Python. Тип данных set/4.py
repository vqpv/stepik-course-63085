string = input()

print(*sorted(set(string), key=string.index), sep='')
