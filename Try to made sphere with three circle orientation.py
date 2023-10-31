from manim import *

class SphereDiagram1(ThreeDScene):
    def construct(self):
        # Main circle representing the sphere
        circle = Circle(radius=2, color=WHITE).set_stroke(width=1)
        dashed_circle_vertical = DashedVMobject(Circle(radius=2, color=WHITE)).rotate(PI / 2)
        dashed_circle_horizontal = DashedVMobject(Circle(radius=1.5, color=WHITE))

        # Axes
        axes = VGroup(
            Arrow(start=[0, -2.5, 0], end=[0, 2.5, 0], color=WHITE),  # y-axis
            Arrow(start=[-2.5, 0, 0], end=[2.5, 0, 0], color=WHITE),  # x-axis
            Arrow(start=[0, 0, -2.5], end=[0, 0, 2.5], color=WHITE)   # z-axis
        )

        # Rho arrow and label
        rho_arrow = Arrow([0, 0, 0], [1.5, 1.5, 0], color=RED, buff=0)
        rho_label = MathTex("\\rho").next_to(rho_arrow.get_end(), UR, buff=0.1)

        # Phi arc and label
        phi_arc = Arc(radius=1.2, start_angle=PI/4, angle=-PI/4, color=GREEN)
        phi_label = MathTex("\\phi").next_to(phi_arc, RIGHT, buff=0.2).shift(0.2*RIGHT)

        # Theta arc and label
        theta_arc = Arc(radius=0.6, start_angle=0, angle=PI/2, color=BLUE)
        theta_label = MathTex("\\theta").next_to(theta_arc, DOWN, buff=0.2)

        # Coordinate labels
        coords_label = VGroup(
            Tex("x").next_to(axes[1], RIGHT),
            Tex("y").next_to(axes[0], UP),
            Tex("z").next_to(axes[2], UP)
        )

        # Animations
        self.play(Create(circle))
        self.play(Create(dashed_circle_horizontal), Create(dashed_circle_vertical))
        self.play(FadeIn(axes), FadeIn(coords_label))
        self.play(Create(rho_arrow), Write(rho_label))
        self.play(Create(phi_arc), Write(phi_label))
        self.play(Create(theta_arc), Write(theta_label))
        self.wait(2)
