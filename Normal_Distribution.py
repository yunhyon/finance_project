#Homework
#Find a way to plot the multiple lines with different colors and label them with std values
'''
https://www.google.com/search?q=normal+distribution&rlz=1C1CHBF_enUS845US845&sxsrf=ACYBGNQZcrk0Jnbu-NIHcXKkYKD46edgwg:1581870053710&tbm=isch&source=iu&ictx=1&fir=lhHDHuAryhN-NM%253A%252CNTVbhD7-dDkldM%252C_&vet=1&usg=AI4_-kSaPP1sWfekAudkIPJx53wOPoEGkQ&sa=X&ved=2ahUKEwiTgYeVvdbnAhXOVt8KHa7RDaAQ_h0wAHoECAgQBA#imgrc=lhHDHuAryhN-NM&imgdii=ESriBRLsCkjqiM
'''

import matplotlib.pyplot as plt
import math
start = -1.0
end = 1.0
increment = 0.01

mean = 0
for sd in [math.sqrt(x) for x in [1/32,1/16,1/8,1/4,1/2]]:
    x_value = []
    y_value = []
    for i in range(201):
        x = start + i * increment
        y = (1 / (sd * math.sqrt(2 * math.pi))) * math.exp((-0.5) * (x - mean) ** 2 / (2 * sd**2))
        x_value.append(x)
        y_value.append(y)
    plt.plot(x_value, y_value)
print(x_value)
print(y_value)

plt.show()