from string import ascii_lowercase

alphabet = {j: i + 1 for i, j in enumerate(ascii_lowercase)}

for i, j in alphabet.items():
    print(i, j)
