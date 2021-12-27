city = input()

countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}
info = f'ERROR: Country for {city} not found'

for country, cities in countries.items():
    if city in cities:
        info = f'INFO: {city} is a city in {country}'
        break

print(info)
