taxi_drivers = dict()

string = input()

while "конец" not in string:
    taxi_driver, score = string.split(', ')
    if taxi_drivers.get(taxi_driver, None):
        taxi_drivers[taxi_driver][0] += 1
        taxi_drivers[taxi_driver][1] += int(score)
    else:
        taxi_drivers[taxi_driver] = [1, int(score)]
    string = input()

for t, s in taxi_drivers.items():
    taxi_drivers[t] = s[1] / s[0]

taxi_drivers = sorted(taxi_drivers.items(), key=lambda x: (-x[1], x[0]))

for driver in taxi_drivers:
    print(*driver)
