n = int(input())
lst = input().split()

def reverse_list(lst, r_ls=[]):
    if lst:
        r_ls.append(lst[-1])
        reverse_list(lst[:-1], r_ls)
    return r_ls

print(*reverse_list(lst))
