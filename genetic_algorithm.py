from audioop import reverse
from hashlib import new
from operator import ne
from color import Color
from crossbreed import *
from selection import *
from mutation import *
import math


def genetic_algorithm(population, target):
    gen = 0
    population.sort(key=lambda x: x.fitness, reverse=True)

    while gen < 100:
        new_population = []
        # crosbreed
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

        print("popu before mutation")
        for individual in new_population:
            print(individual)   

        #mutamos los que tengan bajo fitness
                    
        i = 0
        while i < len(new_population) and new_population[i].setFitness(target) < 0.15:
            candidate = new_population[i]
            if not is_in_pop(new_population, candidate.mutate()):
                new_population[i].mutate()
                new_population[i].setFitness(target)
            i = i + 1

        # nos quedamos con los mejores de la vieja poblacion 
        # personalized_mutation(new_population, population)
        uniform_mutation(new_population, population)

        #seleccionamos 
        elite_selection(new_population)

        # fijarse condicion de corte (fitness)
        if(new_population[0].fitness > 0.95):
            print("done")
            return new_population[0]

        print("after mutation")
        for individual in new_population:
            print(individual)  
        population = new_population
        gen += 1

    return new_population[0]