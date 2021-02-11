import time
from turtle import Screen
from food import Food
from scoreboard import Score
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


<<<<<<< HEAD
=======

>>>>>>> 0530d7b... Initial commit
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.sum_score()

#  detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
<<<<<<< HEAD
        game_is_on = False
        score.game_over()
=======
        score.reset()
        snake.reset()
>>>>>>> 0530d7b... Initial commit

# detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
<<<<<<< HEAD
            game_is_on = False
            score.game_over()
=======
            score.reset()
            snake.reset()

>>>>>>> 0530d7b... Initial commit
screen.exitonclick()
