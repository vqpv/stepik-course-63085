string = input()

for _ in range(len(string) // 2):
    string = string.replace('()', '')
    string = string.replace('[]', '')
    string = string.replace('{}', '')

print("YES" if len(string) == 0 else "NO")
