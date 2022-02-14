n = int(input())

oscar = dict()

for _ in range(n):
    actor = input()
    if oscar.get(actor, None):
        oscar[actor] += 1
    else:
        oscar[actor] = 1

maximum = max(oscar.items(), key=lambda x: x[1])
minimum = min(oscar.items(), key=lambda x: x[1])

if oscar:
    print(*maximum, sep=', ')
    print(*minimum, sep=', ')
