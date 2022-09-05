from audioop import reverse
from hashlib import new
from operator import ge, ne
from color import Color
from crossbreed import *
from selection import selection
from mutation import *
import math
import random
from config_loader import selection_name, max_gens, expected_fit

red_coordinates = []
green_coordinates = []
blue_coordinates = []
color_fit_coordinates = []
closest_color = Color(0, 0, 0)

def validate_expected_fit():
    if (not expected_fit == "default") and (0 <= expected_fit <= 1):
        return expected_fit
    return 0.95


def genetic_algorithm(population, target):
    expected_fitness = validate_expected_fit()
    closest_fit = 0
    
    gen = 0
    max : float
    
    while gen < (max_gens):
        new_population = []

        # crossbreed
        n_iterations = math.floor(len(population) / 2)
        j=0
        for c in range(n_iterations):
            one = population[j]
            two = population[j+1]
            j = j+2
            child1, child2 = uniform_crossbreed(one,two)
            
            flag1 = True
            flag2 = True
            for individual in new_population:
                if child1.equals(individual):
                    flag1 = False
                if child2.equals(individual):
                    flag2 = False
            
            if child1.equals(child2) or flag1:
                new_population.append(child1)
            elif flag2:
                new_population.append(child2)

        if (len(population) % 2 ) == 1:
            child1, child2 = uniform_crossbreed(population[j], population[0])
            flag1 = True
            flag2 = True
            for individual in new_population:
                if child1.equals(individual):
                    flag1 = False
                if child2.equals(individual):
                    flag2 = False
            
            if child1.equals(child2) or flag1:
                new_population.append(child1)
            elif flag2:
                new_population.append(child2)

        #mutamos los que tengan bajo fitness   
        i = 0
        while i < len(new_population) and new_population[i].getFitness(target) < 0.15:
            candidate = new_population[i]
            if not is_in_pop(new_population, candidate.mutate()):
                new_population[i].mutate()
                new_population[i].getFitness(target)
            i = i + 1

        # nos quedamos con los mejores de la vieja poblacion 
        # personalized_mutation(new_population, population, target)
        uniform_mutation(new_population, population, target)
        
        #seleccionamos (seleccion default -> rank)
        selection(new_population, target)

        max = new_population[0]

        for individual in new_population:
            if individual.getFitness(target) > max.getFitness(target):
                max = Color(individual.red, individual.green, individual.blue)

        if(max.getFitness(target) >= expected_fitness):
            print("found at generation:")
            print(gen)
            return max

        if(max.getFitness(target) > closest_fit):
            closest_color = Color(max.red, max.green, max.blue)
            closest_fit = closest_color.getFitness(target)
            print("UPDATE")
            print(gen)
            print(closest_color)
            print("fitness")
            print(closest_color.getFitness(target))
            
    
        color_fit_coordinates.append(closest_color.getFitness(target))

        if(not is_in_pop(new_population, closest_color)):
            new_population.append(Color(closest_color.red, closest_color.green, closest_color.blue))

        print(closest_color.getFitness(target))
        population = new_population
        gen += 1

    print("could not complete algorithm in " + str(gen) + " generations")
    return closest_color