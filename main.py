import numpy as np
import sys
import matplotlib.pyplot as plt
from color import *
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

plt.imshow([[(result.red / 255, result.green / 255, result.blue / 255)],
            [(target_color.red / 255, target_color.green / 255, target_color.blue / 255)]])
plt.show()