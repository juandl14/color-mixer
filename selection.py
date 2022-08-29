from color import Color

def elite_selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)

def roulette_selection(population):
    total_fitness = sum(individual.fitness for individual in population) 
