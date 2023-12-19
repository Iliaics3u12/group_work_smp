def fibonacci(n):
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
