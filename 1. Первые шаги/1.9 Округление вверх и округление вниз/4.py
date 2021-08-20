from math import ceil

L, W, H = map(int, input().split())

print(ceil(((L + W) * H * 2) / 16))
