string = input()

nums = []

for char in string:
    if char.isdigit():
        nums.append(int(char))

print(len(nums), sum(nums))
