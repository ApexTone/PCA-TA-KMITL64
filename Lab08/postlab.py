def fib_iter(n):
    if n <= 0:
        raise ValueError("Fibonacci's Sequence starts at 1")
    fibo = [1, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[n-1]


def fib_rec(n):
    if n <= 0:
        raise ValueError("Fibonacci's Sequence starts at 1")
    if n <= 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def main():
    num = 6
    print(fib_rec(num))
    print(fib_iter(num))