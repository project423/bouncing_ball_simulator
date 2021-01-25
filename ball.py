from turtle import Turtle
from random import randint, uniform, choice

COLORS = ["red", "blue", "yellow", "orange", "green", "white", "purple"]
SHAPES = ["circle", "triangle", "square"]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(choice(COLORS))
        self.penup()
        self.speed(0)
        self.x = randint(-290, 290)
        self.y = randint(200, 400)
        self.goto(self.x, self.y)
        self.dy = 0
        self.dx = uniform(-.1,.1)
        self.da = uniform(-.1,.1)

    
    def bounce_y(self):
        self.color(choice(COLORS))
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reverse(self):
        self.da *= -1
    
    def change_color(self):
        self.color(choice(COLORS))