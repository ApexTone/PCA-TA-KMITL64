def users7():
    file = open('users7.txt', 'r')
    for line in file:
        username, password = line.strip().split()
        print(username, password)


def users1000():
    file = open('users1000.txt', 'r')
    for line in file:
        username, password = line.strip().split()
        print(username, password)


def main():
    users1000()


if __name__ == '__main__':
    main()
