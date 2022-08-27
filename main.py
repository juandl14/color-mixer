import numpy as np
from color import Color
import sys
from genetic_algorithm import genetic_algorithm

colors_from_palette = []
target_color : Color

with open('color_palette.txt') as f:
    first_line = f.readline()
    red, green, blue = first_line.split()
    target_color = Color(int(red), int(green), int(blue))
    for line in f:
        red, green, blue = line.split()
        current_color = Color(int(red), int(green), int(blue))
        colors_from_palette.append(current_color)
f.close()


# print(target_color)


result = genetic_algorithm(colors_from_palette, target_color)

print(result)
print(result.fitness)

# for c in colors_from_palette:
#     print(c.getFitness(target_color))