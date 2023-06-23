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

# test 1430D6E5-5E48-4309-86BD-D863EFBD67E4
# test 2394DD5C-CA07-4E2D-9AE0-3719EC85CDBC
# test 7F2E9FCC-A920-4376-B92F-F385FC6BC304
# test A367F202-E01C-4459-92D6-D0206CDEB68F
# test 52291AAB-B928-41A6-BF14-26F346FDD498
