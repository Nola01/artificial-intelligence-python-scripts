"""
GA with a very simple fitness function
"""

import random

POPULATION_SIZE = 10
GENES = "01"
GENE_LENGTH = 15 
MUTATION_RATE = 0.1
GENERATIONS = 300

""" 
return how many times '1' appears in the individual given
 """
def fitness(individual):
    return individual.count('1')

""" 
return a string combining random genes, as much as the length given
 """
def create_individual(length):
    return ''.join(random.choice(GENES) for _ in range(length))

""" 
return a list of individuals (population) as large as the size given.
Each individual has the same number of genes as the length given
 """
def create_population(size, length):
    return [create_individual(length) for _ in range(size)]

""" 
create a list with the weight of each individual in the population.
Calculate the sum of all weights.
If it is 0, return a random individual from the population
 """
def select_parents(population):
    weights = [fitness(individual) for individual in population]
    total_weight = sum(weights)
    if total_weight == 0:
        return random.choices(population, k=2)
    return random.choices(population, weights=weights, k=2)

""" 
create a random int between 1 and (parent1's length -1) so it will be 
the crossover point. Then it returns a child from the crossover between
parent1 and parent2
 """
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child
""" 
for each gene from an individual, if a random number is minor than the
mutation rate, then this gene's value change to 1. If it's 0, it will be
0. It returns the mutated individual
 """
def mutate(individual):
    mutated = list(individual)
    for i in range(len(mutated)):
        if random.random() < MUTATION_RATE:
            mutated[i] = '1' if mutated[i] == '0' else '0'
    return ''.join(mutated)

""" 
this function creates a population with a specific size and gene length.
For each generation, it creates a new population (childs) selecting 
parents from the current population. In the next iteration, it will
work with this new population (next generation).
Then it finds the best individual in the current population, as well as
his fitness. If the fitness is the same as the max fitness, it found the
perfect individual so it does not need to keep searching among more
generations.
If it does not find the perfect individual, it returns the individual
with max fitness among the last generation.
 """
def genetic_algorithm():
    population = create_population(POPULATION_SIZE, GENE_LENGTH)
    max_fitness = GENE_LENGTH
    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population
        
        best_individual = max(population, key=fitness)
        best_fitness = fitness(best_individual)
        print(f"Generation {generation}: Best Individual = {best_individual}, Fitness = {best_fitness}")
        
        if best_fitness == max_fitness:
            print(f"Perfect individual found in generation {generation}. Ending early.")
            break

    return max(population, key=fitness)

if __name__ == "__main__":
    best_solution = genetic_algorithm()
    print(f"\nBest solution found: {best_solution}, Fitness: {fitness(best_solution)}")
