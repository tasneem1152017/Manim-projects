from manim import *
import numpy as np

class My3DPlot(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        def func(x, y):
            return np.sin(x + y ** 2)

        def region(u, v):
            return u ** 2 + v ** 2 < 3

        # Define the surface
        surface = Surface(
            lambda u, v: np.array([u, v, func(u, v)]),
            resolution=(50, 50),
            u_range=[-2, 2],
            v_range=[-2, 2]
        ).set_style(fill_opacity=0.5, fill_color=BLUE, stroke_color=GREEN)

        # Define the filling at the bottom
        bottom_surface = Surface(
            lambda u, v: np.array([u, v, -1]),
            resolution=(50, 50),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_opacity=0.5,
            fill_color=ORANGE,
            stroke_color=ORANGE
        )

        # Add region limit to the surface
        for mob in surface.family_members_with_points():
            mob.apply_function(lambda p: p if region(p[0], p[1]) else np.array([p[0], p[1], -1]))

        for mob in bottom_surface.family_members_with_points():
            mob.apply_function(lambda p: p if region(p[0], p[1]) else np.array([p[0], p[1], -1.1]))

        self.add(axes)
        self.play(Create(surface))  # Animate the surface coming into view
        self.play(Create(bottom_surface))  # Animate the bottom filling coming into view
