from manim import *
import numpy as np

class SphereMotion1(ThreeDScene):
    def construct(self):
        # Set the camera orientation for 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create a sphere using Surface
        sphere = Surface(
            lambda u, v: np.array([
                np.cos(u) * np.cos(v),
                np.sin(u) * np.cos(v),
                np.sin(v)
            ]), u_range=[0, TAU], v_range=[-PI / 2, PI / 2]
        )

        # Set opacity for the sphere
        sphere.set_fill(BLUE, opacity=0.3)

        # Create the XYZ axes
        axes = ThreeDAxes()

        # Create a moving point on the sphere
        moving_dot = Dot3D(radius=0.05, color=YELLOW)

        # Create a ValueTracker for the angle
        tracker = ValueTracker(0)

        # Function to update the point's position
        def update_dot(mob):
            alpha = tracker.get_value()  # Latitude and Longitude
            phi = alpha  # Latitude

            x = np.cos(alpha) * np.cos(phi)
            y = np.sin(alpha) * np.cos(phi)
            z = np.sin(phi)

            mob.move_to([x, y, z])

        # Create latitude and longitude lines
        latitude_line = Circle(radius=np.cos(tracker.get_value()), color=RED).add_updater(
            lambda m: m.become(Circle(radius=np.cos(tracker.get_value()), color=RED))
        )
        longitude_line = ParametricFunction(
            lambda t: np.array([np.cos(tracker.get_value()) * np.cos(t),
                                np.sin(tracker.get_value()) * np.cos(t),
                                np.sin(t)]),
            t_range=[-PI / 2, PI / 2], color=GREEN
        ).add_updater(
            lambda m: m.become(
                ParametricFunction(
                    lambda t: np.array([np.cos(tracker.get_value()) * np.cos(t),
                                        np.sin(tracker.get_value()) * np.cos(t),
                                        np.sin(t)]),
                    t_range=[-PI / 2, PI / 2], color=GREEN
                )
            )
        )

        # Add everything to the scene
        self.add(sphere, axes, moving_dot, latitude_line, longitude_line)

        moving_dot.add_updater(update_dot)
        self.play(tracker.animate.set_value(TAU), run_time=5, rate_func=linear)
        moving_dot.clear_updaters()
