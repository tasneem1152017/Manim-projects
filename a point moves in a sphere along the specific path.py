from manim import *
import numpy as np

class SphereMotion(ThreeDScene):
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

        # Set a constant latitude (phi)
        constant_phi = PI / 4

        # Function to update the point's position
        def update_dot(mob, alpha):
            theta = alpha * TAU  # Longitude
            phi = constant_phi  # Latitude, kept constant

            x = np.cos(theta) * np.cos(phi)
            y = np.sin(theta) * np.cos(phi)
            z = np.sin(phi)

            mob.move_to([x, y, z])
        
        # Add the sphere, axes, and moving point to the scene
        self.add(sphere, axes, moving_dot)

        # Animate the point moving along a single latitude on the sphere
        self.play(UpdateFromAlphaFunc(moving_dot, update_dot, run_time=5, rate_func=linear))
