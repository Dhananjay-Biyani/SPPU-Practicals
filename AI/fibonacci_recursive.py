def fibonacci_recur(n):
    if n < 0:
        return -1, 0
    if n == 0 or n == 1:
        return n, 1
    fib1, steps1 = fibonacci_recur(n-1)
    fib2, steps2 = fibonacci_recur(n-2)
    return fib1 + fib2, steps1 + steps2 + 1

n = 10
result, steps = fibonacci_recur(n)
print(f"The {n}-th Fibonacci number is {result}, and it took {steps} steps to calculate.")
