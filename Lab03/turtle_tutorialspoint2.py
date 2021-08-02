import turtle


def circle(radius=50):
    t = turtle.Turtle()
    t.circle(radius)
    turtle.done()


def venn(radius=10):
    t = turtle.Turtle()
    for i in range(10):
        t.circle(radius*i)
    turtle.done()


def spiral(radius=10):
    t = turtle.Turtle()
    for i in range(50):
        t.circle(radius+i, 45)   # 45 = central angle (how much the spiral "drift")
    turtle.done()


def concentric(radius=10):
    t = turtle.Turtle()
    for i in range(50):
        t.circle(radius*i)
        t.up()  # lift the pen (no drawing trace)
        t.sety((radius*i)*(-1))
        t.down()  # put down the pen
    turtle.done()


def filled_star():
    t = turtle.Turtle()
    t.fillcolor('orange')
    t.begin_fill()  # fill the enclosed area below (MUST enclosed)
    for i in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()  # stop the filling process
    turtle.done()


def olympic():
    t = turtle.Turtle()
    t.pensize(6)
    first_row_colors = ['blue', 'black', 'red']
    for i in range(len(first_row_colors)):
        t.penup()
        t.pencolor(first_row_colors[i])
        t.goto(i*110, 0)
        t.pendown()
        t.circle(50)
    second_row_colors = ["", "yellow", "", "green"]
    for i in range(1, 4, 2):
        t.penup()
        t.pencolor(second_row_colors[i])
        t.goto(i * 55, -50)
        t.pendown()
        t.circle(50)


def spider_web():
    t = turtle.Turtle()
    t.speed(0)

    # Code for building radical thread
    for i in range(6):
        t.forward(150)
        t.backward(150)
        t.right(60)

    # Code for building spiral thread
    side = 150
    for i in range(15):  # 15 spirals
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(0)
        t.forward(side)
        t.right(120)
        for j in range(6):  # hexagon
            t.forward(side)
            t.right(60)
        side = side - 10
    turtle.done()


def chessboard(size=800):
    t = turtle.Turtle()
    t.speed(8)

    # draw border
    for i in range(4):
        t.forward(size)
        t.right(90)

    block_size = size/8

    b = 0  # alternate col color
    for i in range(8):  # for each column
        a = 1 if b == 0 else 0  # alternate row color
        for j in range(8):  # for each row
            t.penup()
            t.goto(j*block_size, -i*block_size)
            t.pendown()
            if a == 0:
                t.fillcolor('black')
                a = 1
            else:
                t.fillcolor('white')
                a = 0
            t.begin_fill()
            for k in range(4):
                t.forward(block_size)
                t.right(90)
            t.end_fill()
        b = 1 if b == 0 else 0
    turtle.done()


def tally(score=9):
    t = turtle.Turtle()
    t.right(90)
    for i in range(1, score+1):
        if i % 5 == 0:  # completed tally
            t.right(135)
            t.forward(30*(2**0.5))
            t.right(225)
        else:
            t.penup()
            t.goto((i-1)*10, 0)
            t.pendown()
            t.forward(30)
    turtle.done()


def draw_car():
    car = turtle.Turtle()

    # body
    car.color('#2B2BF6')  # outline (line) color
    car.fillcolor('#2B2BF6')
    car.penup()
    car.goto(0, 0)
    car.pendown()
    car.begin_fill()
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.end_fill()

    # roof
    car.penup()
    car.goto(100, 50)
    car.pendown()
    car.setheading(45)
    car.forward(70)
    car.setheading(0)
    car.forward(100)
    car.setheading(-45)
    car.forward(70)
    car.setheading(90)
    car.penup()
    car.goto(200, 50)
    car.pendown()
    car.forward(49.50)

    # wheels
    car.penup()
    car.goto(100, -10)
    car.pendown()
    car.color('#000000')
    car.fillcolor('#000000')
    car.begin_fill()
    car.circle(20)
    car.end_fill()
    car.penup()
    car.goto(300, -10)
    car.pendown()
    car.color('#000000')
    car.fillcolor('#000000')
    car.begin_fill()
    car.circle(20)
    car.end_fill()

    car.hideturtle()


def snowman():
    t = turtle.Turtle()

    def draw_circle(color, radius, x, y):
        t.penup()
        t.fillcolor(color)
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

    # Below three statements for drawing snowman body
    draw_circle("#ffffff", 30, 0, -40)
    draw_circle("#ffffff", 40, 0, -100)
    draw_circle("#ffffff", 60, 0, -200)

    draw_circle("#ffffff", 2, -10, -10)  # Drawing left eye
    draw_circle("#ffffff", 2, 10, -10)  # Drawing right eye
    draw_circle("#FF6600", 3, 0, -15)  # Drawing nose

    # Below three statements for drawing buttons
    draw_circle("#ffffff", 2, 0, -35)
    draw_circle("#ffffff", 2, 0, -45)
    draw_circle("#ffffff", 2, 0, -55)

    # Code for drawing left arm
    t.penup()
    t.goto(-15, -35)
    t.pendown()
    t.pensize(5)
    t.goto(-75, -50)
    # Code for drawing right arm
    t.penup()
    t.goto(15, -35)
    t.pendown()
    t.pensize(5)
    t.goto(75, -50)

    # Code for drawing hat
    t.penup()
    t.goto(-35, 8)
    t.color("black")
    t.pensize(6)
    t.pendown()
    t.goto(35, 8)

    t.goto(30, 8)
    t.fillcolor("black")
    t.begin_fill()
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(15)
    t.end_fill()


def main():
    snowman()


if __name__ == '__main__':
    main()

