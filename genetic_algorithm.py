from audioop import reverse
from hashlib import new
from operator import ne
from color import Color
from crossbreed import *
from selection import *
import math


def genetic_algorithm(population, target):
    gen = 0
    new_population = []

    while gen < 20:
        population.sort(key=lambda x: x.fitness, reverse=True)
        print('After sorted')

        n_iterations = math.floor(len(population) / 2)

        aux_first : Color

        if (len(population) % 2) == 1:
            aux_first = population[0]
        
        j=0
        for c in range(n_iterations):
            one = population[j]
            two = population[j+1]
            j = j+2
            child1, child2 = uniform_crossbreed(one,two)

            new_population.append(child1)
            new_population.append(child2)

        if len(population) == 1:
            child1, child2 = uniform_crossbreed(population[j], aux_first)
            new_population.append(child1)
            new_population.append(child2)

        #mutar --> new_popu = crossbreed
        new_population.sort(key=lambda x: x.fitness)
        i = 0
        while new_population[i].getFitness(target) < 0.15:
            new_population[i].mutate()
            i = i + 1

        # nos quedamos con los mejores de la vieja poblacion 
        new_population.sort(key=lambda x: x.fitness, reverse=True)
        max_fitness = new_population[0].getFitness(target)
        k=0
        while (k < len(population)) and (population[k].getFitness(target) > max_fitness):
            new_population.append(population[k])
            k = k + 1

        #seleccionamos --> new_popu2
        elite_selection(new_population)

        # fijarse condicion de corte (fitness)
        if(new_population[0].getFitness(target) > 0.95):
            print("done")
            return new_population[0]
        gen += 1

    return new_population[0]