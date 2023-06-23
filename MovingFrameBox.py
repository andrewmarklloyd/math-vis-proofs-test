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
E8563ECB-2426-4C36-AF90-C9E9975B287F
E47E25CA-06A0-47B9-B2FB-BEBF431E3A16
28733A66-D9DC-4E82-B6BD-2D94F643FD86
813B468A-E678-4DFA-8A76-0E13A7C1215F
8877C341-F452-48C8-889A-2BE0759C1C05
9E7132B9-E937-45EE-B496-C9364BB242DC
# test 0FC91A09-8010-4705-B262-03AB68AC1EFF
# test 1964EE9E-443E-4FAF-8214-7E921EC982B5
# test CD4BDE8B-FAB9-42F3-BED7-2235F5B2ACE5
# test 6CB7FB21-F2C8-4E8D-8B61-182709591CD1
