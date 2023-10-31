from manim import *

class CreateGraph(Scene):
    def construct(self):
        # ... [Previous code for axes and graphs]

        # Group everything together
        group = VGroup(axes, labels, graph1, graph1_label, graph2, graph2_label, graph3, graph3_label)
        
        # Scale down and move the group to the upper-right corner with a constant scaling factor
        scale_factor = 0.5
        self.play(group.animate.scale(scale_factor).to_corner(UR))
        
        # Display function definitions on the left with adjusted scaling and positioning
        text_scale = 0.7
        fx_label = MathTex("f(x) = \\sqrt{x}").scale(text_scale).to_edge(LEFT).shift(3*UP)
        gx_label = MathTex("g(x) = \\frac{x-3}{2}").scale(text_scale).next_to(fx_label, DOWN, buff=0.5).align_to(fx_label, LEFT)
        combined_function = MathTex("f(x) + g(x) = \\sqrt{x} + \\frac{x-3}{2}").scale(text_scale).next_to(gx_label, DOWN, buff=0.5).align_to(gx_label, LEFT)

        self.play(Write(fx_label))
        self.wait(1)
        self.play(Write(gx_label))
        self.wait(1)
        self.play(Write(combined_function))
        self.wait(1)
        
        # Display properties of the combined function with adjusted scaling and positioning
        properties_title = Text("Properties of f(x) + g(x):").scale(text_scale).next_to(combined_function, DOWN, buff=0.5).to_edge(LEFT)
        prop1 = Text("1. Combination of linear and sqrt function.").scale(0.65).next_to(properties_title, DOWN, buff=0.3).align_to(properties_title, LEFT)
        prop2 = Text("2. Increases monotonically.").scale(0.65).next_to(prop1, DOWN, buff=0.3).align_to(prop1, LEFT)
        prop3 = Text("3. Domain: non-negative real numbers.").scale(0.65).next_to(prop2, DOWN, buff=0.3).align_to(prop2, LEFT)
        
        self.play(Write(properties_title))
        self.play(Write(prop1))
        self.play(Write(prop2))
        self.play(Write(prop3))
        self.wait(2)
