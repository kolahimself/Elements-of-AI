import numpy as np

def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = np.array([5615000, 5439000, 324000, 5080000, 9609000])
    fishers = np.array([1891, 2652, 3800, 11611, 1757])
    
    total_fishers = sum(fishers)
    total_population = sum(populations)
    
    # write your solution here
    population = (fishers/total_fishers) * 100
    
    for country, population in zip(countries, population):
        print("%s %.2f%%" % (country, population)) # modify this to print correct results
    

main()