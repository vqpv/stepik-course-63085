# объявление функции
def print_initials(name, surname, middlename):
    print(f'{surname.capitalize()} {name[0].upper()}.{middlename[0].upper()}.')

# считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print_initials(name, surname, middlename)
