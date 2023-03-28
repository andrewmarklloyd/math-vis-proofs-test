from manim import *

class MovingAround(Scene):
    def construct(self):
        f = open("/tmp/hello.txt", "a")
        f.write("testing!")
        f.close()
        square = Square(color=BLUE, fill_opacity=1)

        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))