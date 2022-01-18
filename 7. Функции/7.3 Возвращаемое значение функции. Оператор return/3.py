def find_duplicate(lst):
    duplicates = []
    for n in lst:
        if lst.count(n) > 1 and n not in duplicates:
            duplicates.append(n)
    return duplicates
