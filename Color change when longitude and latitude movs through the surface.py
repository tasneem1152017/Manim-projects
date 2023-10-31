from manim import *
import numpy as np

class SphereMotion2(ThreeDScene):
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

        def update_line_color(m):
            color = interpolate_color(RED, GREEN, tracker.get_value() / TAU)
            m.set_color(color)

        latitude_line = Circle().add_updater(
            lambda m: m.become(Circle(radius=np.cos(tracker.get_value()))).add_updater(update_line_color)
        )

        longitude_line = ParametricFunction(
            lambda t: np.array([
                np.cos(tracker.get_value()) * np.cos(t),
                np.sin(tracker.get_value()) * np.cos(t),
                np.sin(t)
            ]), t_range=[-PI / 2, PI / 2]
        ).add_updater(
            lambda m: m.become(
                ParametricFunction(
                    lambda t: np.array([
                        np.cos(tracker.get_value()) * np.cos(t),
                        np.sin(tracker.get_value()) * np.cos(t),
                        np.sin(t)
                    ]), t_range=[-PI / 2, PI / 2]
                )
            ).add_updater(update_line_color)
        )

        self.add(sphere, axes, moving_dot, latitude_line, longitude_line)

        moving_dot.add_updater(update_dot)
        self.play(tracker.animate.set_value(TAU), run_time=5, rate_func=linear)
        moving_dot.clear_updaters()
