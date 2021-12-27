n = int(input())

d = {}

for _ in range(n):
    name = input()
    if name in d.keys():
        d[name] += 1
        print(name + str(d[name]))
    else:
        d.update({name: 0})
        print("OK")
