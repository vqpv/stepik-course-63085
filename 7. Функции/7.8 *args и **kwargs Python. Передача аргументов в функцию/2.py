def print_goods(*args):
    count = 0
    for good in args:
        if isinstance(good, str) and good != "":
            count += 1
            print(f"{count}. {good}")
    if count == 0:
        print("Нет товаров")
