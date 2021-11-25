num = input()

for n in sorted(set(num)):
    print(n, num.count(n))
