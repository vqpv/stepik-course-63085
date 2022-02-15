n_1 = int(input())

birthdays = dict()

for _ in range(n_1):
    name, date, month = input().split()
    if birthdays.get(month, None):
        birthdays[month].append(name)
    else:
        birthdays[month] = [name]

n_2 = int(input())

for _ in range(n_2):
    month = input()
    if birthdays.get(month, None):
        print(*sorted(birthdays[month]))
    else:
        print("Нет данных")
