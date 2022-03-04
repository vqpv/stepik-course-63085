number = input()

minimum, maximum = int(number[0]), int(number[0])

while number:
    if int(number[-1]) < minimum:
        minimum = int(number[-1])
    elif int(number[-1]) > maximum:
        maximum = int(number[-1])
    number = number[:-1]

print(minimum)
print(maximum)
