x, y = int(input()), int(input())

while x <= y:
    if x % 2 and x % 3:
        print(x)
    elif x % 777 == 0:
        break
    x += 1
