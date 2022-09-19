from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []  # some segment : Turtle square object
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_new_segment(pos)

    def add_new_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_new_segment(self.segments[-1].position())

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[index - 1].pos()
            self.segments[index].goto(new_pos)
        self.head.fd(20)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(800, 800)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
