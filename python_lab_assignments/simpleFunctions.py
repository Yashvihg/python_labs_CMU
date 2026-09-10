# Name: Yashvi Himanshu Gaglani

def euclid(a, b):

    if a <= 0 or b <= 0:
        print("Both numbers must be positive integers.")
        return None

    while b != 0:
        a, b = b, a % b
    return a


def isbn(digits):

    if not isinstance(digits, (list, tuple)) or len(digits) != 10:
        return False

    total = 0
    for i in range(10):
        d = digits[i]
        if not isinstance(d, int) or d < 0 or d > 10:
            return False
        if d == 10 and i != 9:
            return False
        total += (10 - i) * d

    return total % 11 == 0
