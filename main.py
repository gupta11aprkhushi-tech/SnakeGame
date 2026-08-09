from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food)<15:
        food.refresh()
        screen.update()
        scoreboard.increase()
        snake.extend()
    for i in snake.segment[1:]:
        if snake.head.distance(i)<10:
            scoreboard.game_over()
            game_on=False

    if snake.head.xcor()>=290 or snake.head.xcor()<=-290 or snake.head.ycor()>=290 or snake.head.xcor()<=-290 :
        scoreboard.game_over()
        game_on=False

#commentkhushi123

screen.exitonclick()