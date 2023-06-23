from manim import *

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
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
# test BAEAD43B-FA47-4A6C-A055-6F43F09AF7B0
# test EDA10231-D170-4E65-9F5C-DD4D20961BB3
