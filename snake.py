from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            self.add_segment()

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        if len(self.segments) > 0:
            if self.segments[0].heading() == UP:
                new_segment.goto(self.segments[len(self.segments) - 1].xcor(),
                                 self.segments[len(self.segments) - 1].ycor() - 20)
            if self.segments[0].heading() == DOWN:
                new_segment.goto(self.segments[len(self.segments) - 1].xcor(),
                                 self.segments[len(self.segments) - 1].ycor() + 20)
            if self.segments[0].heading() == RIGHT:
                new_segment.goto(self.segments[len(self.segments) - 1].xcor() - 20,
                                 self.segments[len(self.segments) - 1].ycor())
            if self.segments[0].heading() == LEFT:
                new_segment.goto(self.segments[len(self.segments) - 1].xcor() + 20,
                                 self.segments[len(self.segments) - 1].ycor())
        else:
            new_segment.goto(0, 0)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
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