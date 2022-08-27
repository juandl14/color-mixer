from color import Color

def genetic_algorithm(population, target):

    population.sort(key=lambda x: x.fitness, reverse=True)
    one = population.pop()
    two = population.pop()
    
