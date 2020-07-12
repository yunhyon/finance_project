'''
This script is for the Monte Carlo Simulation
The goal is to estimate pi/4 using monte carlo simulation.

'''
import math
import random

sum = 0
M = 1000
for j in range(M):
    N = 1000000
    n = 0
    for i in range(N):
        x = (random.uniform(0, 1))
        y = (random.uniform(0, 1))
        if math.sqrt(x**2 + y**2) <= 1:
            n = n + 1
    sum = sum + (((n/N) - math.pi/4)**2)
print("the variance is ",sum/M)