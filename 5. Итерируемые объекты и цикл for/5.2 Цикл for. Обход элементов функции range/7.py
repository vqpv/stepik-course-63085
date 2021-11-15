n = int(input())

c_a = 0
c_b = 0

for _ in range(n):
    a, b = input().split()
    if a > b:
        c_a += 1
    else:
        c_b += 1

if c_a > c_b:
    print("Mishka")
elif c_a < c_b:
    print("Chris")
elif c_a == c_b:
    print("Friendship is magic!^^")
