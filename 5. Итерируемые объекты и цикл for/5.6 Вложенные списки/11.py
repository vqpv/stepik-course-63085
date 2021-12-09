n, m = map(int, input().split())

index = 0
maximum = 0
score_sum = 0

for i in range(n):
    score = list(map(int, input().split()))
    for j in range(m):
        if (score[j] > maximum) or (score[j] == maximum and sum(score) > score_sum):
            maximum = score[j]
            score_sum = sum(score)
            index = i

print(index)
