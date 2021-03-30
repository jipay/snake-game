from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.nodes = []
        for _ in range(3):
            self.add_nodes()
        self.head = self.nodes[0]

    def add_nodes(self):
        new = Turtle()
        new.penup()
        new.shape("square")
        new.color("white")
        if len(self.nodes) > 0:
            last = self.nodes[len(self.nodes) - 1]
            if self.nodes[0].heading() == UP:
                new.goto(last.xcor(), last.ycor() - 20)
            if self.nodes[0].heading() == DOWN:
                new.goto(last.xcor(), last.ycor() + 20)
            if self.nodes[0].heading() == RIGHT:
                new.goto(last.xcor() - 20, last.ycor())
            if self.nodes[0].heading() == LEFT:
                new.goto(last.xcor() + 20, last.ycor())
        else:
            new.goto(0, 0)
        self.nodes.append(new)

    def reset(self):
        for n in self.nodes:
            n.goto(1000, 1000)
        self.nodes.clear()
        for _ in range(3):
            self.add_nodes()
        self.head = self.nodes[0]

    def move(self):
        for index in range(len(self.nodes) - 1, 0, -1):
            self.nodes[index].goto(self.nodes[index - 1].xcor(), self.nodes[index - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
