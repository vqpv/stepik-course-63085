def check_password(password):
    nums = [i for i in password if i.isdigit()]
    upper_letters = [i for i in password if i.isupper()]
    special_chars = [i for i in password if i in "!@#$%*"]
    condition = len(nums) >= 3 and upper_letters and special_chars and len(password) >= 10
    print("Perfect password" if condition else "Easy peasy")
