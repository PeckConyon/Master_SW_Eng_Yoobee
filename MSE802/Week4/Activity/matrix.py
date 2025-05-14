#QC Activity
#1. Ask user to input x and y for two vectors
#2. Convert vectors to polar coordinates
#3. Apply all operators ( addition, subtraction, division, multiplication, power) to the above
#4. Show results of all by graph

import numpy as np
import matplotlib.pyplot as plt
import re

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
    magnitudes = np.abs(vector) #this function can even get an array of complex numbers
    angles = np.angle(vector) #np. absolute()   in radians
    return (magnitudes, angles)  # [(r1, θ1), (r2, θ2)]

def vector_operations(v1, v2):
    return {
        'Addition': v1 + v2,
        'Subtraction': v1 - v2,
        'Multiplication': v1 * v2,
        'Division': np.divide(v1, v2, where=v2 != 0),  
        'Power': np.power(v1, v2)
    }
    # Got RuntimeWarning: divide by zero encountered in divide  when no filtering when division for np.divide(v1, v2)
     

def plot_vectors(results):
    plt.figure(figsize=(10, 7))
    origin = [0], [0]

    for label, vec in results.items():
        # Plot using real parts only (imaginary can't be shown in 2D XY)
        #print(f'imaginary part x {vec[0].imag}' )
        #print(f'imaginary part y {vec[1].imag}' )
        x = vec[0].real
        y = vec[1].real
        plt.quiver(*origin, x, y, angles='xy', scale_units='xy', scale=1, label=label)

    plt.xlim(-20, 20)
    plt.ylim(-20, 20)

    plt.grid()
    plt.legend()
    plt.title("Vector Operation Results")
    plt.xlabel("Real X")
    plt.ylabel("Real Y")
    plt.show()


try:
    while True:
        print("\n=== Vector Operations ===")

        v1 = get_vector("Vector 1")
        v2 = get_vector("Vector 2")

        polar_v1 = to_polar(v1)
        polar_v2 = to_polar(v2)

        print("\nPolar Coordinates:")
        for i in range(2):
            print(f"Vector 1[{i}]: magnitude = {polar_v1[0][i]:.2f}, theta = {np.degrees(polar_v1[1][i]):.2f} degrees")
            print(f"Vector 2[{i}]: magnitude = {polar_v2[0][i]:.2f}, theta = {np.degrees(polar_v2[1][i]):.2f} degrees")

        results = vector_operations(v1, v2)

        print("\nVector Operation Results:")
        for key, value in results.items():
            print(f"{key}: {value}")

        # Plot results
        plot_vectors(results)
        
        print("\nPress CTRL + C  and press ENTER to exist")

except KeyboardInterrupt:
    print("\nExited by user.")
