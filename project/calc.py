def fact(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def gcd(a, b):
    if a == 0 and b != 0:
        return abs(b)
    elif a != 0 and b == 0:
        return abs(a)
    elif a == 0 and b == 0:
        return 0

    a = abs(a)
    b = abs(b)
    while b != 0:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r
