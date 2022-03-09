letters = list(input())

while letters:
    if letters[0] in ("a", "e"):
        print("Ага! Нашлась")
        break
    print(f"Текущая буква: {letters[0]}")
    letters.pop(0)

if not letters:
    print("Распечатали все буквы")
