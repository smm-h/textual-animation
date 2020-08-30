
from math import sin, cos, pi
from os import get_terminal_size
from random import random, choice

input("PRESS ENTER")

width, height = get_terminal_size()

screen = {}

colors = "░▒▓█"


class Ball():
    def __init__(self):
        self.trail = [(random() * width, random() * height)]
        self.trailLimit = 32
        self.direction = random() * pi * 2
        self.deviation = random() / 64
        self.speed = random() / 2 + 0.001

    def progress(self):
        self.direction += self.deviation
        x = self.trail[0][0] + cos(self.direction) * self.speed
        y = self.trail[0][1] - sin(self.direction) * self.speed
        while x < 0:
            x += width
        while y < 0:
            y += height
        while x > width:
            x -= width
        while y > height:
            y -= height
        p = (x, y)
        self.trail.insert(0, p)
        if len(self.trail) > self.trailLimit:
            self.trail.pop()

    def pinpoint(self):
        for p in self.trail:
            k = round(p[1]) * width + round(p[0])
            if not k in screen:
                screen[k] = -1
            screen[k] = min(3, screen[k]+1)


pool = [Ball() for i in range(8)]

while True:
    screen.clear()
    for ball in pool:
        ball.progress()
        ball.pinpoint()
    t = ""
    for i in range(width * height):
        if i in screen:
            t += colors[screen[i]]
        else:
            t += " "
    print(t)
