import turtle #is a module for starting games-- this is simpler for beginners
import random
wn = turtle.Screen() #creates a window
wn.title("PongGame!")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0) #what is tracer?

#gotta make paddles
#Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0) #speed of the animation, it sets the speed to max speed, otherwise itl be slow
paddle_1.shape("square")
paddle_1.color("blue")
paddle_1.shapesize(stretch_wid =5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)
#Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0) #speed of the animation, it sets the speed to max speed, otherwise itl be slow
paddle_2.shape("square")
paddle_2.color("blue")
paddle_2.shapesize(stretch_wid =5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# ok what abt the ball
ball = turtle.Turtle()
ball.speed(0) #speed of the animation, it sets the speed to max speed, otherwise itl be slow
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

#let's make the paddles move!
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

#how can we use this to make the paddle move? we need to do keyboard binding

wn.listen()
wn.onkeypress(paddle_1_up, "w")

#ok lets do for rest
def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

wn.listen()
wn.onkeypress(paddle_1_down, "s")

wn.listen()
wn.onkeypress(paddle_2_up, "Up")

wn.listen()
wn.onkeypress(paddle_2_down, "Down")
#let's make the main loop for the game

while True:
    wn.update() #updates/restarts the screen

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking now
    if ball.ycor() > 290:
        ball.sety(-290)
        ball.setx(random.randint(-290, 290))
        ball.dx *= random.choice([-1, 1])
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        #if this occurs we also need to add one for point total
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        #if this occurs we need to add one to right team's point total
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() -40):
          ball.setx(340)
          ball.dx *=-1 #aka it changes courses
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() -40):
          ball.setx(-340) #what is this line doing?
          ball.dx *=-1 #aka it changes courses