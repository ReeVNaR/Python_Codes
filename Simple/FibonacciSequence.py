def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example
print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]
