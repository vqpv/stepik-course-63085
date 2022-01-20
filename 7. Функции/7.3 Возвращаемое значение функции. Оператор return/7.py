def factorial(number: int):
    m = 1
    for i in range(2, number + 1):
        m *= i
    return m

def trailing_zeros(n: int) -> int:
    s_n = str(factorial(n))
    new_s_n = s_n.rstrip('0')
    return len(s_n) - len(new_s_n)
