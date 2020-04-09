'''   
Pong Game created by Riol Malaj 
    by watcching the freecodecamp.org tutorial
'''

import turtle, random

#GLOBAL VAR
ball_speed = 0.2
paddle_speed = 10

#GAME INIT
window = turtle.Screen()
window.title("Pong by @TheRiolDeal")
window.bgcolor("#111111")
window.setup(800, 600)
window.tracer(0)

def create_model(model, s, x, y = 0):
    model.speed(0)
    model.shape("square")
    model.shapesize(s,1)
    model.color("#EEEEEE")
    model.penup()
    model.goto(x, y)

#Paddle A
paddle_a = turtle.Turtle()
create_model(paddle_a, 5, -350)
paddle_a.score = 0

#Paddle B
paddle_b = turtle.Turtle()
create_model(paddle_b, 5, 350)
paddle_b.score = 0

#Ball
ball = turtle.Turtle()
create_model(ball, 1, 0)
ball.dx = random.randint(-1, 1) * ball_speed
ball.dy = random.randint(-1, 1) * ball_speed

# Pen
pen = turtle.Turtle()
pen.hideturtle()
create_model(pen, 1, 0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#FUNCTIONS
paddle_a_up = lambda : paddle_a.sety(paddle_a.ycor() + paddle_speed)
paddle_a_down = lambda : paddle_a.sety(paddle_a.ycor() - paddle_speed)
paddle_b_up = lambda : paddle_b.sety(paddle_b.ycor() + paddle_speed)
paddle_b_down = lambda : paddle_b.sety(paddle_b.ycor() - paddle_speed)

def restart_ball():
    ball.goto(0, 0)
    ball.dx = random.randint(-1, 1) * ball_speed
    ball.dy = random.randint(-1, 1) * ball_speed

def restart_game():
    pen.clear()
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    paddle_a.score = 0
    paddle_b.score = 0
    restart_ball()

#KEY BINDING
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
window.onkeypress(restart_ball, "b")
window.onkeypress(restart_game, "r")

#Main game loop:
while True:
    window.update()
    if ball.dx == 0 or ball.dy == 0:
        ball.dy = random.randint(-1, 1) * ball_speed
        ball.dx = random.randint(-1, 1) * ball_speed
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        paddle_a.score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(paddle_a.score, paddle_b.score), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        paddle_b.score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(paddle_a.score, paddle_b.score), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() > 330 and ball.xcor() < 340 and ball.ycor() < (paddle_b.ycor() + 60) and  ball.ycor() > (paddle_b.ycor() - 60):
        ball.setx(330)
        ball.dx *= -1

    if ball.xcor() < -330 and ball.xcor() > -340 and ball.ycor() < (paddle_a.ycor() + 60) and  ball.ycor() > (paddle_a.ycor() - 60):
        ball.setx(-330)
        ball.dx *= -1

window.exitonclick()