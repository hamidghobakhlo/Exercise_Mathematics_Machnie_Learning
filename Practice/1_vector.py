import numpy as np 
import matplotlib.pyplot as plt

vec1 = []
vec2 = []

# Input from user 
for i in range(1, 3):
    a = input(f"Enter number {i} for vector 1: ")
    b = input(f"Enter number {i} for vector 2: ")
    vec1.append(a)
    vec2.append(b)

# Convert list to INT
try:
    vec1 = list(map(int, vec1))
    vec2 = list(map(int, vec2))
except ValueError:
    print("Please enter number!")
    exit()

# Checking the length of a vector
if len(vec1) != len(vec2):
    print("len(Vector1) == len(Vector2)")
    exit()

# Add function
def add(vec1, vec2):
    result = np.add(vec1, vec2)  
    print("Sum: ", result)

# Subtract function
def subtract(vec1,vec2):
    result = np.subtract(vec1,vec2)
    print("Subtract: ",result)

# Multiply function
def multiply(vec1, vec2):
    result = np.multiply(vec1, vec2)  
    print("Multiply: ", result)

# Main function
def main(vec1, vec2):
    add(vec1, vec2)
    subtract(vec1,vec2)
    multiply(vec1, vec2)

# Function call
main(vec1, vec2)