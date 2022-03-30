#pong
import turtle

window = turtle.Screen()
window.title("Pong The Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#score
ScoreA = 0
ScoreB = 0

#paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

#paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = -0.15

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 18, "normal"))

#Functions
def paddleA_up():
    y = paddleA.ycor()
    y +=20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -=20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y +=20
    paddleB.sety(y)    

def paddleB_down():
   y = paddleB.ycor()
   y -=20
   paddleB.sety(y)   

#Key Bindings
window.listen()
window.onkeypress(paddleA_up, "w")
window.onkeypress(paddleA_down, "s")
window.onkeypress(paddleB_up, "Up")
window.onkeypress(paddleB_down, "Down")

#Main Game Loop
while True:
    window.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        ScoreA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(ScoreA, ScoreB), align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        ScoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(ScoreA, ScoreB), align="center", font=("Courier", 18, "normal"))

    #paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1