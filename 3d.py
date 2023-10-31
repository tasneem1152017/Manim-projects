from manim import *

class SineSurface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            z_range=[-1, 1, 1]
        ).scale(0.6)  # Scale down the axes

        surface = Surface(
            lambda u, v: axes.c2p(u, v, np.sin(u + v ** 2)),
            u_range=[-3, 3],
            v_range=[-2, 2],
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(20, 20),
            fill_opacity=0.7,  # Adjust the opacity
            fill_color=[BLUE, GREEN]  # Gradient color
        ).scale(0.6)  # Scale down the surface

        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        self.add(axes)
        self.play(Create(surface))
        self.wait(2)
