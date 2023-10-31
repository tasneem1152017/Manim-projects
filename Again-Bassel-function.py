from manim import *
import numpy as np
from scipy.special import jn

class BesselPlotWithDescription(Scene):
    def construct(self):
        colors = [BLUE, GREEN, RED, ORANGE]

        # Create Axes and Graphs
        axes = Axes(
            x_range=[0, 10],
            y_range=[-1, 1],
            axis_config={"color": BLUE},
        )
        labels = axes.get_axis_labels()
        graphs = []
        for n in range(4):
            graph = axes.plot(
                lambda x: jn(n, x),
                color=colors[n]
            )
            graphs.append(graph)
        
        # Create Fills
        fills = []
        for graph in graphs:
            fill = axes.get_area(graph, x_range=[0, 10], opacity=0.2)
            fills.append(fill)

        plot_group = VGroup(axes, labels, *graphs, *fills)

        # Create Description Text
        description_text = Text("""
            This plot shows the first four Bessel functions:
            \( J_0(x) \), \( J_1(x) \), \( J_2(x) \), and \( J_3(x) \).
            The area under each curve is also shaded.
        """)
        description_text.scale(0.4)
        
        # Animate
        self.play(Create(axes), Write(labels))
        for graph, fill in zip(graphs, fills):
            self.play(Create(graph), Create(fill))

        self.wait(1)

        # Scale down and move plot
        self.play(
            plot_group.animate.scale(0.5).to_edge(UP + RIGHT)
        )
        
        # Display description on the left side
        self.play(
            Write(description_text.next_to(plot_group, LEFT).align_to(plot_group, UP))
        )

        self.wait(1)
