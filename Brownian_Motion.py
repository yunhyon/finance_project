#1. you generate t values:[0.0, 0.1,..., 10.0]
#2. You generate W values:[W(0), W(0.1), ..., W(10)] by using the formula
# W(t+delta_t) = W(t) + Z(0,0.1).
# That is W(0.1) = W(0) + Z(0,0.1), W(0.2) = W(0.1) + Z(0,0.1)

import matplotlib.pyplot as plt
import random
import math

delta_t = 0.01
start = 0
end = 10.0

for j in range(30):
    t_value = [0.0]
    W_value = [0.0]  # by definition of Brownian motion, W(0) = 0
    W_current = 0.0  # W(0)
    for i in range(1,1001): #the simulation starts from W(0.01)
        t = start + i*delta_t
        t_value.append(t)
        Z = random.normalvariate(0.0, math.sqrt(delta_t)) # Generating independent Normal random variable, N(0, 0.01)
        #print(t, W_current, Z)
        W_current = W_current + Z # By definition of BM, W(0.01) = W(0) + Z1(0,0.01), W(0.02) = W(0.01) + Z2(0,0.01),..., W(10) = W(9.99)+ Z1000(0,0.01)
        W_value.append(W_current) # W(t+delta_t) = W(t) + Z(0,0.1)

    plt.plot(t_value,W_value)
plt.show()
