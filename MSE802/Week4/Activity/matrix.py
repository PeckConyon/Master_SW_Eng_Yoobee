#QC Activity
#1. Ask user to input x and y for two vectors
#2. Convert vectors to polar coordinates
#3. Apply all operators ( addition, subtraction, division, multiplication, power) to the above
#4. Show results of all by graph

import numpy as np
import matplotlib.pyplot as plt
import re
from qiskit.visualization import plot_bloch_vector


# Regex pattern to reject any letters except 'j'
INVALID_COMPLEX_PATTERN = re.compile(r"[a-ik-z]")  # disallow a–i and k–z

def read_complex(prompt):
    while True:
        user_input = input(prompt).strip().lower()

        # Reject any letters except 'j'
        if INVALID_COMPLEX_PATTERN.search(user_input):
            print("Invalid input. Only 'j' is allowed as imaginary unit (e.g., 3+2j, 4j, -1-3j, or just 5).")
            continue

        try:
            return complex(user_input)
        except ValueError:
            print("Invalid format. Please enter a valid real or complex number (e.g., 2, -3.5, 4j, 2+3j).")

def get_vector(name):
    x = read_complex(f"Enter x for {name}: ")
    y = read_complex(f"Enter y for {name}: ")
    return np.array([x, y], dtype=complex)

def to_polar(vector):
    #sqrt(a^2 + b^2)
    magnitude = np.abs(vector) #this function can even get an array of complex numbers
    theta = np.angle(vector) #np. absolute()   in radians
    return magnitude, theta  # [(r1, θ1), (r2, θ2)]

def vector_operations(v1, v2):
    return {
        'Addition': v1 + v2,
        'Subtraction': v1 - v2,
        'Multiplication': v1 * v2,
        'Division': np.divide(v1, v2, where=v2 != 0),  
        'Power': np.power(v1, v2)
    }
    # Got RuntimeWarning: divide by zero encountered in divide  when no filtering when division for np.divide(v1, v2)
     

def plot_vectors_in_cartizian(results, v1, v2):
    colors = ['blue', 'green', 'red']  # v1, v2, result

    for label, result_vector in results.items():
        plt.figure(figsize=(6, 5))
        origin = [0], [0]

        v1c = v1[0] + v1[1]
        v2c = v2[0] + v2[1]
        result = result_vector[0] + result_vector[1]

        x_vals = [v1c.real, v2c.real, result.real]
        y_vals = [v1c.imag, v2c.imag, result.imag]
        vector_labels = ['Vector 1', 'Vector 2', label]

        for i in range(3):
            plt.quiver(*origin, x_vals[i], y_vals[i], angles='xy', scale_units='xy', scale=1,
                       color=colors[i], label=vector_labels[i])

        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.grid()
        plt.title(f"{label} Operation")
        plt.xlabel("Real")
        plt.ylabel("Imaginary")
        plt.legend()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()



try:
    while True:
        print("\n=== Vector Operations ===")

        v1 = get_vector("Vector 1")
        v2 = get_vector("Vector 2")
        
        print(f'Vector 1 : {v1}')
        print(f'Vector 2 : {v2}')

        magnitude1, theta1  = to_polar(v1)
        magnitude2, theta2  = to_polar(v2)

        print("\nPolar Coordinates:")
        for i in range(2):
            print(f"Vector 1[{i}]: magnitude = {magnitude1}, theta = {np.degrees(theta1)} degrees")
            print(f"Vector 2[{i}]: magnitude = {magnitude2}, theta = {np.degrees(theta2)} degrees")

        results = vector_operations(v1, v2)

        print("\nVector Operation Results:")
        for key, value in results.items():
            print(f"{key}: {value}")

        # Plot results
        plot_vectors_in_cartizian(results, v1, v2)
        
  
        
        print("\nPress CTRL + C  and press ENTER to exist")

except KeyboardInterrupt:
    print("\nExited by user.")
