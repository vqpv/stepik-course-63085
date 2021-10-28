n = int(input())
m = list(str(input()))

while "1" in m and "0" in m:
    m.remove("1")
    m.remove("0")

print(len(m))
