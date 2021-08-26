def mystery1_rec(lst):  # this function find max number in a list
    if len(lst) == 1:
        return lst[0]
    a = lst[0]
    b = mystery1_rec(lst[1:])
    return a if a > b else b


def mystery1_iter(lst):
    high = -float('inf')
    for num in lst:
        if high < num:
            high = num
    return high


def multiply_rec(a, b):
    pass


def palindrome_rec(line):
    pass


def main():
    lst = [66, 999, 123, 85, 12, 33, 59, 85123, 456, 789]
    print(mystery1_iter(lst))
    print(mystery1_rec(lst))