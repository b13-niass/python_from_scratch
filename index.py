# La suite de Fibonacci : 0, 1, 1, 2, 3, 5, 8, ...
# fib(n) = fib(n-1) + fib(n-2), avec fib(0) = 0 et fib(1) = 1
def fibonacci(n):
    if n == 0:  # Cas de base
        return 0
    elif n == 1:  # Cas de base
        return 1
    else:  # Appel récursif
        return fibonacci(n - 1) + fibonacci(n - 2)

print("10e nombre de Fibonacci :", fibonacci(10))  # Output: 55