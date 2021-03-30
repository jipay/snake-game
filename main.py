from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake py Gamu!")
screen.tracer(0)
# new = Turtle()
# new.penup()
# new.shape("square")
# new.color("white")
mySnake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(mySnake.up, "Up")
screen.onkey(mySnake.down, "Down")
screen.onkey(mySnake.left, "Left")
screen.onkey(mySnake.right, "Right")
is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    mySnake.move()
    if mySnake.head.distance(food) < 15:
        food.refresh()
        score.add(1)
        mySnake.add_nodes()

    if mySnake.head.xcor() > 280 or mySnake.head.xcor() < -280 or mySnake.head.ycor() > 280 or mySnake.head.ycor() < -280:
        print("GAME OVER.")
        is_on = False
        score.game_over()

    for s in mySnake.segments[1:]:
        if mySnake.head.distance(s) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
