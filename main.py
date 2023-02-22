import time
import ball
import paddle
import scoreboard
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen_ball = ball.Ball()
score = scoreboard.Scoreboard()

game_is_active = True
while game_is_active:
    screen.update()
    time.sleep(screen_ball.ball_speed)
    screen_ball.move()

    if screen_ball.ycor() > 280 or screen_ball.ycor() < -280:
        screen_ball.bounce_wall()

    if (screen_ball.distance(r_paddle) < 50 and screen_ball.xcor() > 320 or
            screen_ball.distance(l_paddle) < 50 and screen_ball.xcor() < -320):
        screen_ball.bounce_paddle()

    if screen_ball.xcor() > 380:
        screen_ball.reset_position()
        score.l_point()

    if screen_ball.xcor() < -380:
        screen_ball.reset_position()
        score.r_point()

screen.exitonclick()
