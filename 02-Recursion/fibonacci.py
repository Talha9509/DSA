# to find fibonacci no. of given place/index

def fibonacci(n):
    assert n>=0 and int(n)==n, "Fibonacci number can't be negative or non-integer"
    if n<=1:
        # base case n=0 and n=1
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(0))