def fibonacci(n):
    """
    Calculate the n-th number in a modified Fibonacci sequence starting with 1 and 2

    This function assumes a Fibonacci sequence where the first two terms are 1 and 2 and each subsequent term is the sum of the previous two terms.

    :param n: int. The position in the sequence for which to calculate the Fibonacci number
    :return: int. The n-th Fibonacci number in the modified sequence
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(2, n + 1):
            a, b = b, a + b
        return a
