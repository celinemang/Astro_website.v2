from bokeh.plotting import figure, output_file, show
import numpy as np
import math

x = np.arange(0, math.pi*2, 0.05)
y = np.cos(x)
output_file("sine.html")

p = figure(title="Sine Wave Example", x_axis_label='x', y_axis_label='y')
p.line(x, y, line_width=2, legend_label="Sine")  # Set legend_label instead of legend
p.legend.title = "Legend"  # Optional: Set legend title

show(p)
