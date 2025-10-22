from turtle import Turtle
import time

STARTING_POS = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):

        self.body = []
        self.create_snake()
        self.head = self.body[0]
        # self.head.color("white")  # <-- make head color different
        # self.head.shape("square")

    def create_snake(self):
        for position in STARTING_POS:
            self.add_body(position)

    def add_body(self, position):
        """Creates one segment of the snake's body"""
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")  # default body color
        new_segment.goto(position)
        self.body.append(new_segment)

    def move(self):
        for body_num in range(len(self.body) -1, 0, -1):
            new_x = self.body[body_num-1].xcor()
            new_y = self.body[body_num-1].ycor()
            self.body[body_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)


    def extend_body(self):
        #extending the snake body when score increases
        self.add_body(self.body[-1].position())



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)




