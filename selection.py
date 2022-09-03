from color import Color
import numpy as np
from config_loader import selection_name

def selection(population):
        match selection_name: 
            case "roulette":
                roulette_selection(population)
            case "elite":
                elite_selection(population)
            case _:
                rank_selection(population)

def elite_selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)

def roulette_selection(population):
    max = sum(individual.fitness for individual in population) 
    probabilities = [individual.fitness / max for individual in population]
    np_array = np.random.choice(list(population), size=len(population)//2, replace=True, p=probabilities)
    population = np_array

def rank_selection(individuals):
    P = len(individuals)
    individuals.sort(key=lambda x: x.fitness, reverse=True)
    f_1 = [(P-i)/i for i in range(1, P+1)]
    sum_f_1 = sum(f_1)
    if sum_f_1 == 0:
        probabilities = [1.0]
    else:
        probabilities = [(f_1[i] / sum_f_1) for i in range(0, P)]
    np_array = np.random.choice(list(individuals), size=P//2, replace=False, p=probabilities)
    individuals = np_array