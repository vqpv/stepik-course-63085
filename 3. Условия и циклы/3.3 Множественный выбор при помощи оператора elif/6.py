pass_1 = input()
pass_2 = input()

if len(pass_1) < 7:
    print("Short")
elif pass_1 != pass_2:
    print("Difference")
else:
    print("OK")
