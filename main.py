
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()


food = Food()
score = Scoreboard()

game_on = True
screen.listen()

screen.onkey(key= "Up", fun=snake.up)
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(key= "Up", fun=snake.up)
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    #detect collision with the food.
    score.write_score()
    if snake.head.distance(food) < 18:
        food.refresh()
        print("wow tasty!!")
        score.clear_score()
        score.add_score()
        snake.extend_body()

    #detect collision with the Wall.
    # if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
    #     game_on = False
    #     score.game_over()

    if snake.head.xcor() > 290:snake.head.goto(-290,snake.head.ycor())
    elif snake.head.xcor() < -290:snake.head.goto(290,snake.head.ycor())
    elif snake.head.ycor() < -290:snake.head.goto(snake.head.xcor(),290)
    elif snake.head.ycor() > 290:snake.head.goto(snake.head.xcor(),-290)



    #detect collision with the tail
    for body in snake.body[1:]:
        if snake.head.distance(body) < 10:
            game_on = False
            score.game_over()




screen.exitonclick()