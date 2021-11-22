nums = list(map(int, input().split()))

pos_nums = [num for num in nums if num > 0]

print(min(pos_nums) if pos_nums else "Empty")
