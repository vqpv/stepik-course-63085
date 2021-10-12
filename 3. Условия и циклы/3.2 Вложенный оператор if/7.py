city_1 = input().lower()
city_2 = input().lower()

if city_1[-1] == 'ь':
    if city_1[-2] == city_2[0]:
        print('Good')
    else:
        print('Bad')
else:
    if city_1[-1] == city_2[0]:
        print('Good')
    else:
        print('Bad')
