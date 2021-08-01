def from_decimal(dec, base):
    if dec < 0:
        return 'Error: negative number'
    if base < 0:
        return 'Error: negative base'
    if base > 36:
        return 'Error: base > 36'
    if base < 2:
        return 'Error: base < 2'

    if dec == 0:
        return '0'

    result = ''
    while dec > 0:
        remainder = dec % base
        dec = dec // base
        # print(dec, remainder)
        if remainder >= 10:
            remainder = chr(remainder - 10 + ord('A'))
            # print('new:', remainder)
        result = str(remainder) + result
    return result


def to_decimal(line, base):
    if line[0] == '-':  # xxx: is there a better way?
        return 'Error: negative number'
    if base < 0:
        return 'Error: negative base'
    if base > 36:
        return 'Error: base > 36'
    if base < 2:
        return 'Error: base < 2'

    result = 0
    line = line[::-1]  # reverse order
    for index, num in enumerate(line):
        num = num.upper()
        if 'A' <= num <= 'Z':
            num = 10 + ord(num) - ord('A')
        num = int(num)

        if num >= base:
            return 'Error: incorrect number/base'

        result += num * (base**index)
    return result


def main():
    print(to_decimal('1BJ', 26))


if __name__ == '__main__':
    main()
