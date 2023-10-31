from manim import *
import numpy as np

class SphereMotion(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        sphere = Surface(
            lambda u, v: np.array([
                np.cos(u) * np.cos(v),
                np.sin(u) * np.cos(v),
                np.sin(v)
            ]), u_range=[0, TAU], v_range=[-PI / 2, PI / 2]
        )
        sphere.set_fill(BLUE, opacity=0.3)

        axes = ThreeDAxes()

        moving_dot = Dot3D(radius=0.05, color=YELLOW)

        tracker = ValueTracker(0)

        def update_dot(mob):
            alpha = tracker.get_value()
            phi = alpha

            x = np.cos(alpha) * np.cos(phi)
            y = np.sin(alpha) * np.cos(phi)
            z = np.sin(phi)

            mob.move_to([x, y, z])

        latitude_line = Circle(radius=np.cos(tracker.get_value()), color=RED)
        longitude_line = ParametricFunction(
            lambda t: np.array([
                np.cos(tracker.get_value()) * np.cos(t),
                np.sin(tracker.get_value()) * np.cos(t),
                np.sin(t)
            ]), t_range=[-PI / 2, PI / 2], color=GREEN
        )

        self.add(sphere, axes, moving_dot, latitude_line, longitude_line)

        moving_dot.add_updater(update_dot)

        # Color update logic
        for t in np.linspace(0, TAU, 100):
            tracker.set_value(t)
            update_dot(moving_dot)

            color = interpolate_color(RED, GREEN, t / TAU)

            latitude_line.set_color(color)
            longitude_line.set_color(color)
            
            self.wait(0.05)
