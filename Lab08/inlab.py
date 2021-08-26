import turtle
t = turtle.Turtle()


def turtle_tree(n):
    angle = 30

    def _tree(num):
        if num > n:
            return
        fw_dist = 200/2**num
        t.forward(fw_dist)

        # left branched
        t.left(angle)
        _tree(num+1)

        # right branches
        t.right(angle*2)
        _tree(num+1)

        # reset
        t.left(angle)
        t.back(fw_dist)

    _tree(0)


def stars1(n):
    def _stars1(num):
        if num <= 0:
            return
        t.up()
        t.goto(0, 10*num)
        t.down()
        t.write('* '*max(num-n, n-num+1))
        _stars1(num - 1)

    _stars1(n*2)


def stars2(n):
    def _stars2(num):
        if num > n*2:
            return
        t.up()
        t.goto(0, -10 * num)
        t.down()
        t.write('* ' * min(num, (n*2)-num+1))
        _stars2(num + 1)

    _stars2(0)


def main():
    n = 5
    # stars1(n)
    # stars2(n)
    turtle_tree(n)
    turtle.done()


if __name__ == '__main__':
    main()
