from turtle import Turtle, Screen
import time

s = Screen()
s.setup(800,600)
s.bgcolor("black")
s.title("Pong Game by KK")
s.tracer(0)

def create_paddle(xpos):
    paddle = Turtle("square")
    paddle.color("white")
    paddle.penup()
    paddle.goto(xpos,0)
    paddle.shapesize(4,1,0)
    return paddle


def player_up():
    if player.ycor() <= 250:
        player.sety(player.ycor() + 10)

def player_down():
    if player.ycor()>=-250:
        player.sety(player.ycor() - 10)


player = create_paddle(-380)
ai = create_paddle(380)    
ai_dy = 3

ball = Turtle("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball_dx, ball_dy=3,3

# Score
score_a = 0
score_b = 0

# Pen
pen = Turtle()
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()



game_is_on = True

while game_is_on:
    time.sleep(1/60)
    s.update()

    #ball move
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)
    if ball.ycor()>290 or ball.ycor()<-290:
        ball_dy = ball_dy*-1 

    #ball out right edge
    if ball.xcor() >= 390: 
        ball.goto(0, 0)
        ball_dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'bold'))

    #ball out left edge
    if ball.xcor() <= -390: 
        ball.goto(0, 0)
        ball_dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'bold'))

 
    #paddle moving
    ai.sety(ai.ycor() + ai_dy)
    if ai.ycor() >= 260 or ai.ycor()<=-260:
        ai_dy = ai_dy * -1

    s.listen()
    s.onkeypress(player_up, "Up")
    s.onkeypress(player_down, "Down")
    
     # Paddle and ball collisions
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < ai.ycor() + 60 and ball.ycor() > ai.ycor() -60):
        ball.setx(340)
        ball_dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < player.ycor() + 60 and ball.ycor() > player.ycor() -60):
        ball.setx(-340)
        ball_dx *= -1

s.exitonclick()