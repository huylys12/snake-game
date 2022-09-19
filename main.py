from turtle import Screen, Turtle
from snake import Snake
from scorebard import ScoreBoard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


def draw_outline():
    drawer = Turtle()
    drawer.hideturtle()
    drawer.color("white")
    drawer.pensize(10)
    drawer.penup()
    drawer.goto(-270, -250)
    drawer.pendown()
    for _ in range(2):
        drawer.forward(540)
        drawer.left(90)
        drawer.forward(480)
        drawer.left(90)


draw_outline()
snake = Snake()
scoreboard = ScoreBoard()
food = Food()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 20:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # detect collision with wall
    pos_head = snake.head.position()
    if pos_head[1] <= -250 or pos_head[1] >= 230 or pos_head[0] <= -270 or pos_head[0] >= 270:
        # game_is_on = False
        time.sleep(1)
        scoreboard.reset_game()
        snake.reset()

    # detect collision with tail
    for seg in snake.segments[-1:1:-1]:
        if snake.head.distance(seg) < 20:
            # game_is_on = False
            time.sleep(1)
            scoreboard.reset_game()
            snake.reset()
            break


screen.exitonclick()
