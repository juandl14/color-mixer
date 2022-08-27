from color import Color

def elite_selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)
