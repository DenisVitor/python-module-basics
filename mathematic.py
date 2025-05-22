def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def factor(n):
    if n < 0:
        return "Fatorial não definido para negativos"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
