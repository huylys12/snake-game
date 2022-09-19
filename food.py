from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_rand = random.randint(-12, 12)
        y_rand = random.randint(-11, 10)
        self.goto(x_rand * 20, y_rand * 20)
