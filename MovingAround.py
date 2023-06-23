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
8877C341-F452-48C8-889A-2BE0759C1C05
9E7132B9-E937-45EE-B496-C9364BB242DC
# test 0FC91A09-8010-4705-B262-03AB68AC1EFF
# test 1964EE9E-443E-4FAF-8214-7E921EC982B5
# test CD4BDE8B-FAB9-42F3-BED7-2235F5B2ACE5
