from string import ascii_uppercase

n = int(input())

print([j * (i + 1) for i, j in enumerate(ascii_uppercase)][:n])
