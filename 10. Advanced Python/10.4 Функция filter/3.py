days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']

filtered_days = list(filter(lambda x: len(x) == 4 or x.startswith('S'), days))

for day in sorted(filtered_days):
    print(day)
