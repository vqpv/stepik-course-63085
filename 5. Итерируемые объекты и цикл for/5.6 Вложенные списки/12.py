n, m = map(int, input().split())

maximum = []

for _ in range(n):
    scores = list(map(int, input().split()))
    maximum.append(max(scores))

best_score = max(maximum)
winner_num = maximum.count(best_score)

print(winner_num)
