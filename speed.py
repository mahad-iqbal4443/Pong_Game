from turtle import Screen, Turtle
turtle = Turtle()
screen = Screen()


class Speed:
    def __init__(self):
        self.a = screen.textinput("Level Selection", "Enter level Easy, Medium, Hard").lower()

    def level(self):
        if self.a == "easy":
            return 0.1
        elif self.a == "medium":
            return 0.09
        elif self.a == "hard":
            return 0.05
        else:
            turtle.color("White")
            turtle.write("Invalid Entry Restart Game", align="center", font=("Courier", 10, "normal"))
            return 0
