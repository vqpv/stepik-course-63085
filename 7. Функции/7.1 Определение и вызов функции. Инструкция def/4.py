def count_letters(string):
    capital_letters = [i for i in string if i.isupper()]
    lowercase_letters = [i for i in string if i.islower()]
    print("Количество заглавных символов:", len(capital_letters))
    print("Количество строчных символов:", len(lowercase_letters))
