num = int(input())
string = input().lower()

count = 26

print("YES" if num >= count and len(set(string)) >= count else "NO")
