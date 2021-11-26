count = int(input())
nums = list(map(int, input().split()))

sorted_nums = []

while nums:
    min_num = min(nums)
    sorted_nums.append(min(nums))
    nums.remove(min(nums))

print(*sorted_nums)
