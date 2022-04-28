from test import Test
from simulation import Simulation
import statistics
from random_solution import generate_random_solution
from data import Data

def run_ten(sim):
    result = []
    for x in range(10):
        result.append(sim.run_simulation(False))
    print("min", min(result), "max",  max(result), "avg", sum(result)/len(result), "std", statistics.stdev(result))



if __name__ == '__main__':
    population_size = 500
    number_of_generations = 50
    is_tournament = True
    selection_parameter = 25
    genes_to_cross = 4
    crossover_probability = 1
    mutation_probability = 0.2
    case = 'hard'
    sim = Simulation(population_size, number_of_generations, is_tournament, selection_parameter, genes_to_cross,
                     crossover_probability, mutation_probability, case)
    sim.run_simulation(plot=True)
    run_ten(sim)






