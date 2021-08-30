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
    if b == 1:
        return a
    return a + multiply_rec(a, b-1)


def palindrome_rec(line):
    def _palindrome_rec(first, last):
        if first > last:
            return True
        if line[first] != line[last]:
            return False
        return _palindrome_rec(first+1, last-1)
    return _palindrome_rec(0, len(line)-1)


def main():
    # lst = [66, 999, 123, 85, 12, 33, 59, 85123, 456, 789]
    # print(mystery1_iter(lst))
    # print(mystery1_rec(lst))
    # print(multiply_rec(50, 3))
    print(palindrome_rec('1221'))


if __name__ == '__main__':
    main()

