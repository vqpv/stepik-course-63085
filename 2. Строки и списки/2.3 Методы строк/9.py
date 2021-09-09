s = input().lower()

s = s.replace('a', '')
s = s.replace('o', '')
s = s.replace('y', '')
s = s.replace('e', '')
s = s.replace('u', '')
s = s.replace('i', '')
s = s.replace('', '.')

print(s[:-1])
