# функция merge_two_list должна объединить два списка
def merge_two_list(a, b):
    new_list = []
    lst = a + b
    while lst:
        new_list.append(lst.pop(lst.index(min(lst))))
    return new_list


# функция merge_sort должна выполнить сортировку
def merge_sort(s):
    if len(s) == 1:
        return s
    return merge_two_list(merge_sort(s[:len(s) // 2]), merge_sort(s[len(s) // 2:]))
