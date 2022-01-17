from functools import reduce

numbers = [int(input()) for i in range(int(input()))]

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

print(reduce(gcd, numbers))
