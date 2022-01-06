string = input()

dictionary = {"Били": set(), "Вили": set(), "Дили": set()}

while string != "конец":
    for key, _ in dictionary.items():
        if key in string:
            dictionary[key].add(string[6:])
    string = input()

sorted_dictionary = sorted(dictionary.items(), key=lambda k: -len(k[1]))

for keys, items in sorted_dictionary:
    print(f'Количество уникальных комментаторов у {keys} -', len(items))
