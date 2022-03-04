number = bin(int(input()))[2:]

while number:
    print(number[-1])
    number = number[:-1]
