import time


# use this decorator to time the execution time
# https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d
def timer(method):
    def timed(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        print(method.__name__, (end_time-start_time) * 1000, "ms")
        return result
    return timed


@timer
def m1(n):  # O(n)
    # don't use sum as a variable name (same as sum() function)
    rounds = 0
    my_sum = 0
    while rounds < n:
        my_sum += 1
        rounds += 1
    return my_sum


@timer
def m2(n):  # O(n)
    rounds = 0
    my_sum = 0
    while rounds < n:
        my_sum += 1
        rounds += 2
    return my_sum


@timer
def m3(n):  # O(n^2)
    round1s = 0
    my_sum = 0
    while round1s < n:
        round2s = 0
        while round2s < n:
            my_sum += 1
            round2s += 1
        round1s += 1
    return my_sum


@timer
def m4(n):  # O(n^2)?
    round1s = 0
    my_sum = 0
    while round1s < n:
        round2s = 0
        while round2s < n:
            my_sum += 1
            round2s += 10
        round1s += 20
    return my_sum


@timer
def m5(n):  # O(n)
    round1s = 0
    my_sum = 0
    while round1s < n:
        my_sum += 1
        round1s += 1
    round2s = 0
    while round2s < n:
        my_sum += 1
        round2s += 1
    return my_sum


@timer
def m6(n):  # O(n^3)?
    round1s = 0
    my_sum = 0
    while round1s < n:
        round2s = 0
        while round2s < n*n:
            my_sum += 1
            round2s += 1
        round1s += 1
    return my_sum


@timer
def m7(n):  # O(n^2)
    round1s = 0
    my_sum = 0
    while round1s < n:
        round2s = 0
        while round2s < round1s:
            my_sum += 1
            round2s += 1
        round1s += 1
    return my_sum


@timer
def m8(n):  # O(n^2)
    round1s = 0
    my_sum = 0
    while round1s < n:
        round2s = 0
        while round2s < round1s*100:
            my_sum += 1
            round2s += 1
        round1s += 1
    return my_sum


@timer
def m9(n):  # O(n^5)
    round1s = 0
    my_sum = 0
    while round1s < n:
        round2s = 0
        while round2s < n * n:
            round3s = 0
            while round3s < round2s:
                my_sum += 1
                round3s += 1
            round2s += 1
        round1s += 1
    return my_sum


@timer
def m10(n):  # O(log n)
    rounds = 1
    my_sum = 0
    while rounds < n:
        my_sum += 1
        rounds *= 2
    return my_sum


@timer
def m11(n):  # O(log n)
    i = n
    my_sum = 0
    while i > 0:
        my_sum += 1
        i /= 2.0
    return my_sum


@timer
def m12(n):  # O(log n): the runtime is log10 n still
    rounds = 1
    my_sum = 0
    while rounds < n:
        my_sum += 1
        rounds *= 10
    return my_sum


def main():
    lst = [10, 50, 100, 500, 1000, 5000, 10000, 20000]
    for n in lst:
        print(f"n = {n}".center(30, "-"))
        m1(n)
        m2(n)
        m3(n)
        m4(n)
        m5(n)
        m6(n)
        m7(n)
        m8(n)
        m9(n)
        m10(n)
        m11(n)
        m12(n)


if __name__ == '__main__':
    main()
