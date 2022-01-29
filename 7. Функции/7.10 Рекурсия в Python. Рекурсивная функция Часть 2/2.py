# функция quick_sort должна выполнить сортировку
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    left = [i for i in lst if i < lst[0]]
    center = [i for i in lst if i == lst[0]]
    right = [i for i in lst if i > lst[0]]
    
    return quick_sort(left) + center + quick_sort(right)
