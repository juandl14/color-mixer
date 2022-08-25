import numpy as np
from color import Color
import sys

colors_from_palette = []

with open('color_palette.txt') as f:
    for line in f:
        [red, green, blue] = line.split()
        current_color = Color(red, green, blue)
        print(current_color)
        np.append(colors_from_palette, current_color)
f.close()

print(colors_from_palette)
