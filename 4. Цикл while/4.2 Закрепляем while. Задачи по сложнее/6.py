n, m = map(int, input().split())

list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

list_3 = list_1 + list_2
list_4 = []

while list_3:
    list_4.append(min(list_3))
    list_3.remove(min(list_3))

print(*list_4)
