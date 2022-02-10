subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]

sorted_subject_marks = sorted(subject_marks, key=lambda x: x[1])

for mark in sorted_subject_marks:
    print(*mark)
