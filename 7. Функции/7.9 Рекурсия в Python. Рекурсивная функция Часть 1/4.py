def flatten(lst):
    new_list = []
    for i in lst:
        if isinstance(i, int):
            new_list.append(i)
        else:
            new_list += flatten(i)
    return new_list
