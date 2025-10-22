from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.speed("fastest")
        randomx = random.randint(-280,280)
        randomy = random.randint(-280, 280)
        self.goto(x=randomx, y=randomx)
        self.refresh()

    def  refresh(self):
        randomx = random.randint(-280, 280)
        randomy = random.randint(-280, 280)
        self.goto(x=randomx, y=randomx)
