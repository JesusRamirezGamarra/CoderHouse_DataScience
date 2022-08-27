def fibonaccy(n):
    print (n)
    return n if n == 1 or n == 0 else fibonaccy(n-1) + fibonaccy(n-2)

print(fibonaccy(3))