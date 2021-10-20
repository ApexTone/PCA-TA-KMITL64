from bin_tree import BST, Node


def get_users7():
    file = open('users7.txt', 'r')
    lst = []
    for line in file:
        username, password = line.strip().split()
        lst.append((username, password))
    return lst


def get_users1000():
    file = open('users1000.txt', 'r')
    lst = []
    for line in file:
        username, password = line.strip().split()
        lst.append((username, password))
    return lst


def main():
    login_tree = BST()
    print('Loading users...')
    users = get_users1000()
    for user in users:
        login_tree.insert(Node(user[0], user[1]))
    print(f'Users loaded successfully: {login_tree.tree_size()} records')
    username = input('Login with username: ')
    credential = login_tree.find(username)
    if credential is not None:
        for i in range(3):
            password = input('Enter password: ')
            if credential.password == password:
                print('Successfully logged in')
                quit()
        print('Too many failed login attempts')
        login_tree.remove(username)
    else:
        print('No user in the list')


if __name__ == '__main__':
    main()
