c = int(input())
nums = list(map(int, input().split()))

for i in range(1, c):
    i_num = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > i_num:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = i_num

print(*nums)
