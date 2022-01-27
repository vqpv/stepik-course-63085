def list_sum_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + list_sum_recursive(lst[1:])
