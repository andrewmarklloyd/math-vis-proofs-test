from manim import *

class MovingAround(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=1)
        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))

# test update
# test 1430D6E5-5E48-4309-86BD-D863EFBD67E4
# test 2394DD5C-CA07-4E2D-9AE0-3719EC85CDBC
