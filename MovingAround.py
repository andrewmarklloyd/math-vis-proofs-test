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
E47E25CA-06A0-47B9-B2FB-BEBF431E3A16
28733A66-D9DC-4E82-B6BD-2D94F643FD86
813B468A-E678-4DFA-8A76-0E13A7C1215F
