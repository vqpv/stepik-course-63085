num = int(input())

n = num
answer = "Yes"

if num == 0 or num == 1 or num > 999999:
    answer = "No"
else:
    while n > 2:
        if num % (n - 1) == 0:
            answer = "No"
            break
        else:
            n -= 1

print(answer)
