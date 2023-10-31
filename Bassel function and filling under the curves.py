from manim import *
import numpy as np
from scipy.special import jn  # For the Bessel functions

class BesselPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10.5], 
            y_range=[-0.5, 0.7], 
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))

        colors = [YELLOW, ORANGE, RED, GREEN]

        # This function returns the Bessel function values
        def bessel_function(n, x):
            return jn(n, x)

        # Plotting the Bessel functions and animating them
        for n in range(4):
            graph = axes.plot(lambda x: bessel_function(n, x), color=colors[n])
            fill = axes.get_area(graph, color=colors[n], opacity=0.3)
            self.play(Create(graph), FadeIn(fill), run_time=2)
        
        self.wait(1)
