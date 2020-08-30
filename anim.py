
from os import get_terminal_size
from time import sleep
from enum import Enum

palette = " ░▒▓█"

width, height = get_terminal_size()

emptyFrame = (" " * width) * height


class PlayProcession(Enum):
    once = 0
    loop = 1
    boomerang = 2


class Animation():
    def __init__(self):
        self.frames = []

    def play(self, direction=+1, play=PlayProcession.once, delay=0.5):

        frame = 0
        n = len(self.frames) - 1

        while True:
            print(self.frames[frame])
            sleep(delay)
            frame += direction

            if play == PlayProcession.once:
                if frame == n or frame == 0:
                    break

            elif play == PlayProcession.loop:
                if frame == 0:
                    frame = n
                if frame == n:
                    frame = 0

            elif play == PlayProcession.boomerang:
                if frame == n or frame == 0:
                    direction = -direction


class Fade(Animation):
    def __init__(self):
        super().__init__()

        for color in palette:
            self.frames.append((color * width) * height)


class Glisten(Animation):
    def __init__(self):
        super().__init__()

        self.frames.append(emptyFrame)

        phase = 0

        while True:
            frame = ""

            self.frames.append(frame)
            if phase == 0:

                phase += 1
            elif phase == 1:
                phase += 1
            elif phase == 2:
                phase += 1
            else:
                break

        for i in range(width + height):
            pass

        for color in palette:
            pass


class Sparkle(Animation):
    # +xo.`´
    def __init__(self):
        super().__init__()

        for i in 100:
            self.frames.append((self.line() * width) * height)


animation = Fade

animation().play(play=PlayProcession.boomerang)
