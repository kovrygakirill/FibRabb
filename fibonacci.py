def fib(number):
    fib1 = fib2 = 1
    for i in range(2, number):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2 if number > 0 else 0
