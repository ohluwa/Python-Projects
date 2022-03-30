#pong
import turtle
import winsound

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