from audioop import reverse
from hashlib import new
from operator import ne
from color import Color
from crossbreed import *
from selection import *
import math


def genetic_algorithm(population, target):
    gen = 0
    population.sort(key=lambda x: x.fitness, reverse=True)

    while gen < 5:
        new_population = []

        print('After sorted')

        n_iterations = math.floor(len(population) / 2)

        aux_first : Color
        print("Population size")
        print(len(population))

        if (len(population) % 2) == 1:
            aux_first = population[0]
        
        j=0
        for c in range(n_iterations):
            one = population[j]
            two = population[j+1]
            j = j+2
            child1, child2 = uniform_crossbreed(one,two)
            
            flag1 = True
            flag2 = True
            for individual in new_population:
                print(child1)
                print(child2)
                print(individual)
                if child1.equals(individual):
                    flag1 = False
                if child2.equals(individual):
                    flag2 = False
            
            if flag1:
                new_population.append(child1)
            if flag2:
                new_population.append(child2)

                

        if len(population) == 1:
            child1, child2 = uniform_crossbreed(population[j], aux_first)
            if child1 not in new_population:
                new_population.append(child1)
            if child2 not in new_population:
                new_population.append(child2)

        #mutar --> new_popu = crossbreed
                    
        i = 0
        while i < len(new_population) and new_population[i].setFitness(target) < 0.15:
            new_population[i].mutate()
            new_population[i].setFitness(target)
            i = i + 1

        # nos quedamos con los mejores de la vieja poblacion 
        new_population.sort(key=lambda x: x.fitness, reverse=True)
        print(len(new_population))
        k=0
        while (k < math.floor(len(population)/2)) and (population[k].fitness > 0.5):
            new_population.append(population[k])
            k = k + 1

        #seleccionamos --> new_popu2
        elite_selection(new_population)

        # fijarse condicion de corte (fitness)
        if(new_population[0].fitness > 0.95):
            print("done")
            return new_population[0]

        population = new_population
        gen += 1

    return new_population[0]