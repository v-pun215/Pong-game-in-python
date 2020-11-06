import turtle

wn = turtle.Screen()
wn.title("Pong game by Vihaan Pundir")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle a
a = turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("white")
a.shapesize(stretch_wid=5, stretch_len=1)
a.penup()
a.goto(-350, 0)

# Paddle b
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("white")
b.shapesize(stretch_wid=5, stretch_len=1)
b.penup()
b.goto(350, 0)


# Ball
ba = turtle.Turtle()
ba.speed(0)
ba.shape("square")
ba.color("white")
ba.penup()
ba.goto(0, 0)
ba.dx = 0.3
ba.dy = -0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))



#Function
def a_up():
    y = a.ycor()
    y += 20
    a.sety(y)

def a_down():
    y = a.ycor()
    y -= 20
    a.sety(y)

def b_up():
    y = b.ycor()
    y += 20
    b.sety(y)

def b_down():
    y = b.ycor()
    y -= 20
    b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(a_up, "w")
wn.onkeypress(a_down, "s")
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")





# Main Game loop
while True:
    wn.update()

    # Move the ball
    ba.setx(ba.xcor() + ba.dx)
    ba.sety(ba.ycor() + ba.dy)

    # Border Checking
    if ba.ycor() > 290:
        ba.sety(290)
        ba.dy *= -1

    if ba.ycor() < -290:
        ba.sety(-290)
        ba.dy *= -1

    if ba.xcor() > 390:
        ba.goto(0, 0)
        ba.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ba.xcor() < -390:
        ba.goto(0, 0)
        ba.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # P and b collisitions..
    if (ba.xcor() > 340 and ba.xcor() < 350) and (ba.ycor() < b.ycor() + 40 and ba.ycor() > b.ycor() -40):
        ba.setx(340)
        ba.dx *= -1

    if (ba.xcor() < -340 and ba.xcor() > -350) and (ba.ycor() < a.ycor() + 40 and ba.ycor() > a.ycor() -40):
        ba.setx(-340)
        ba.dx *= -1
