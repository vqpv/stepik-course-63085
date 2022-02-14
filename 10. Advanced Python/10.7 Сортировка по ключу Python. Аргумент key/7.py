n_1 = int(input())

phone_book = dict()

for _ in range(n_1):
    phone, name = input().split()
    if phone_book.get(name, None):
        phone_book[name].append(phone)
    else:
        phone_book[name] = [phone]

n_2 = int(input())

for _ in range(n_2):
    name = input()
    if phone_book.get(name, None):
        print(*phone_book[name])
    else:
        print("Неизвестный номер")
