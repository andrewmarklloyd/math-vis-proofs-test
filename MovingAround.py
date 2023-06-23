from manim import *

class MovingAround(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=1)
        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))

# test update
E8563ECB-2426-4C36-AF90-C9E9975B287F
