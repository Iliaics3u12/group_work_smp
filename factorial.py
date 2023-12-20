def factorial(n):
    """
    This function calculates the factorial of a non-negative integer n.

    :param n: int
    :return: int
    """
    if n < 0:
        return "Input should be a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact
