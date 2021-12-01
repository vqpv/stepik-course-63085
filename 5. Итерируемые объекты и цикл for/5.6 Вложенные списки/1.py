n = int(input())

a = []
s = 0

for i in range(n):
    nums = input().split()
    a.append(nums)
    s += int(a[i][i])

print(s)
