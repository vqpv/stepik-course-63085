boys_count = int(input())
boys_skills = sorted(map(int, input().split()))
girls_count = int(input())
girls_skills = sorted(map(int, input().split()))

pairs = 0

while boys_skills and girls_skills:
    if abs(boys_skills[0] - girls_skills[0]) <= 1:
        pairs += 1
        boys_skills.pop(0)
        girls_skills.pop(0)
    else:
        if boys_skills[0] > girls_skills[0]:
            girls_skills.pop(0)
        elif boys_skills[0] < girls_skills[0]:
            boys_skills.pop(0)

print(pairs)
