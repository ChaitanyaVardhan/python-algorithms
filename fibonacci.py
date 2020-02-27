import time
import sys


def fib_n(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_n(n-1) + fib_n(n-2)
    return result


def fib_memoize(n, memoize):
    if n == 1 or n == 2:
        result = 1
        memoize[n-1] = result
    elif memoize[n-1]:
        result = memoize[n-1]
    else:
        result = fib_memoize(n-1, memoize) + fib_memoize(n-2, memoize)
        memoize[n-1] = result
    return result
    

def fib_bottom_up(n):
    fib_arr = [None] * n
    fib_arr[0] = 1
    fib_arr[1] = 1
    i = 2
    while i < n:
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]
        i += 1
    return fib_arr[n-1]


if __name__ == "__main__":
    n = int(sys.argv[1])
    start = time.time()
    y = fib_n(n)
    end = time.time()
    print(f"fib_n {n} = {y} Time taken = {end-start}")
    

    memoize = [None] * (n+1)
    start = time.time()
    y = fib_memoize(n, memoize)
    end = time.time()
    print(f"fib_memoize {n} = {y} Time taken = {end-start}")

    start = time.time()
    y = fib_bottom_up(n)
    end = time.time()
    print(f"fib_bottom_up {n} = {y}  Time taken = {end-start}")
