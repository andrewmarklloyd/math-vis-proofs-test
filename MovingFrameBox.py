from manim import *

class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()

# test 1430D6E5-5E48-4309-86BD-D863EFBD67E4
# test 2394DD5C-CA07-4E2D-9AE0-3719EC85CDBC
# test 7F2E9FCC-A920-4376-B92F-F385FC6BC304
# test A367F202-E01C-4459-92D6-D0206CDEB68F
