numbers = [char for char in input() if char.isdigit()]
repeating_numbers = [num for num in numbers if numbers.count(num) > 1]

if repeating_numbers:
    print(*sorted(set(repeating_numbers)) if repeating_numbers else "NO")
else:
    print("NO")
