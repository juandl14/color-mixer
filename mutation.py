from color import Color
import math
import numpy

def mutate(color):
    #elegir numero random de 0 a 255
    return numpy.random.randint(0,255)

def is_in_pop(pop, candidate):
    for individual in pop:
        if individual.equals(candidate):
            return True
    return False
    
def personalized_mutation(new_population, population, target):
    new_population.sort(key=lambda x: x.getFitness(target), reverse=True)
    k=0
    while (k < math.floor(len(population)/2)) and (population[k].getFitness(target) > 0.5):
        if not is_in_pop(new_population, population[k]):
            new_population.append(population[k])
        k = k + 1

def uniform_mutation(new_population, population, target):
    old_color : Color
    for individual in population:
        if numpy.random.uniform() < 0.5:
            old_color = individual
            i = 0
            for i in range(3):
                if i == 1 and numpy.random.uniform() > 0.5:
                    individual.red = mutate(individual.red)
                elif i ==2 and numpy.random.uniform() > 0.5:
                    individual.green = mutate(individual.green)
                elif numpy.random.uniform() > 0.5:
                    individual.blue = mutate(individual.blue)
            
            if not is_in_pop(new_population, individual):
                new_population.append(individual)
