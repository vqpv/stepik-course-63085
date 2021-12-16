n, m = map(int, input().split())

color = "#Black&White"

for _ in range(n):
    string = input().split()
    for c in string:
        if c in ['C', 'M', 'Y', 'G']:
            color = "#Color"

print(color)
