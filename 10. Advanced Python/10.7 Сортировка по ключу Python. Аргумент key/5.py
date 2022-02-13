goods = []

string = input()

while "конец" not in string:
    good, price = string.split(': ')
    goods.append([good, int(price)])
    string = input()

sorted_goods = sorted(goods, key=lambda x: x[1])

for g in reversed(sorted_goods):
    print(g[0])
