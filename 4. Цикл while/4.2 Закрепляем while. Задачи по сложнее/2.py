password_1 = input()

while True:
    password_2 = input()
    if 5 <= len(password_2) <= 9:
        password_1 = password_2
        continue
    else:
        break

print(password_1)
