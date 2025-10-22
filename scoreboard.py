from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 270)



    def add_score(self):
        self.score += 1
        print(self.score)
        return self.score

    def game_over(self):
        self.goto(0,0)
        self.write(("Game Over"), move=False, align=ALIGNMENT, font=('Courier', 20, 'normal'))


    def write_score(self):

        self.write((f"Score = {self.score}"), move=False, align=ALIGNMENT, font=FONT)

    def clear_score(self):
        self.clear()