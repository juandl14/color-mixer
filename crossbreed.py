import sys
import numpy
from color import Color

# def crossbreed(one, two):

BITS_NUM = 8
getbinary = lambda x, n: format(x, 'b').zfill(n)

def uniform_crossbreed(parent1, parent2, ):
    child_red1, child_red2 = uniform_crossbreed_per_color(parent1.red, parent2.red)
    child_green1, child_green2 = uniform_crossbreed_per_color(parent1.green, parent2.green)
    child_blue1, child_blue2 = uniform_crossbreed_per_color(parent1.blue, parent2.blue)

    child1 = Color(child_red1, child_green1, child_blue1)
    child2 = Color(child_red2, child_green2, child_blue2)

    return child1, child2

def uniform_crossbreed_per_color(component1, component2):
    child_bin1 = getbinary(component1, 8)
    child_bin2 = getbinary(component2, 8)

    for i in range(8):
        if numpy.random.uniform() > 0.5:
            aux = child_bin1[i]
            child_bin1 = child_bin1[:i] + child_bin2[i] + child_bin1[i + 1:]
            child_bin2 = child_bin2[:i] + aux + child_bin2[i + 1:]

    return int(child_bin1, 2), int(child_bin2, 2)
