def perimeter(n):
    a, b, total = 0, 1, 0
    for i in range(n + 1):
        total += b
        a, b = b, a + b
    return total * 4
