import numpy as np
from color import *
import sys
from genetic_algorithm import genetic_algorithm
from config_loader import file

target_color : Color
generation_output : int

colors_from_palette = []
with open(file, 'r') as f:
    first_line = f.readline()
    red, green, blue = first_line.split()
    target_color = Color(int(red), int(green), int(blue))
    for line in f:
        red, green, blue = line.split()
        current_color = Color(int(red), int(green), int(blue))
        current_color.setFitness(target_color)
        colors_from_palette.append(current_color)
f.close()


result = genetic_algorithm(colors_from_palette, target_color)

print(result)
print(result.fitness)
# print(generation_output)

# for c in colors_from_palette:
#     print(c.getFitness(target_color))