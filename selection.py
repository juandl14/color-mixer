from color import Color
import numpy as np


def elite_selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)

def roulette_selection(population):
    max = sum(individual.fitness for individual in population) 
    probabilities = [individual.fitness / max for individual in population]
    np_array = np.random.choice(list(population), size=len(population)//2, replace=True, p=probabilities)
    population = np_array