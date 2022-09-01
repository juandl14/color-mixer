import json

f = open('./config.json')

data = json.load(f)
file = data['file']
selection_name = data['selection']
max_gens = data['max_generations']
expected_fit = data['expected_fitness']


f.close()