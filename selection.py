from color import Color
import numpy as np
from config_loader import selection_name
import math

def selection(population, target):
        match selection_name: 
            case "roulette":
                roulette_selection(population, target)
            case "elite":
                elite_selection(population, target)
            case _:
                rank_selection(population, target)

def elite_selection(population, target):
    population.sort(key=lambda x: x.getFitness(target), reverse=True)
    population = population[0:math.ceil(len(population)/2)]

def roulette_selection(population, target):
    max = sum(individual.getFitness(target) for individual in population) 
    probabilities = [individual.getFitness(target) / max for individual in population]
    np_array = np.random.choice(list(population), size=len(population)//2, replace=True, p=probabilities)
    population = np_array

def rank_selection(individuals, target):
    P = len(individuals)
    individuals.sort(key=lambda x: x.getFitness(target), reverse=True)
    f_1 = [(P-i)/i for i in range(1, P+1)]
    sum_f_1 = sum(f_1)
    if sum_f_1 == 0:
        probabilities = [1.0]
    else:
        probabilities = [(f_1[i] / sum_f_1) for i in range(0, P)]
    np_array = np.random.choice(list(individuals), size=P//2, replace=False, p=probabilities)
    individuals = np_array