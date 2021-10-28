n, m = map(int, input().split())
s_1 = list(map(int, input().split()))
s_2 = list(map(int, input().split()))

s_3 = s_1 + s_2
s_4 = []

while s_3:
    s_4.append(min(s_3))
    s_3.remove(min(s_3))

print(*s_4)
