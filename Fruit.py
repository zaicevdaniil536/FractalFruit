import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_fruit():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    fruit = f.generate()
    # Add noise to the fractal shape to make it look more like fruit
    noise = np.random.normal(0, 0.05, fruit.shape)
    fruit = fruit + noise
    fruit = np.clip(fruit, 0, 1)
    # Apply a fruit-like color map to the fractal shape
    fruit = plt.cm.YlOrBr(fruit)
    # Return the fractal fruit
    return fruit

# Generate 10 fractal fruit images
for i in range(10):
    fruit = generate_fractal_fruit()
    plt.imsave("fractal_fruit_{}.png".format(i), fruit)
