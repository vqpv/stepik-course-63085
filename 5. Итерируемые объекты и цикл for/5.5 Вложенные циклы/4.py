c = int(input())
nums = list(map(int, input().split()))

count = 0

for i in range(c - 1):
    for j in range(c - i - 1):
        if nums[j] > nums[j + 1]:
            count += 1
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(*nums)
print(count)
