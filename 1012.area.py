"""
BeeCrowd Problem 1012 - Area
Calculates areas for different geometric shapes based on three input values.
"""

# Constants
PI = 3.14159

# 1. Input: Read three floating-point values from a single line
# input().split() breaks the string into a list, map(float, ...) converts them
a, b, c = map(float, input().split())

# 2. Calculations: Applying geometric formulas
triangle = (a * c) / 2
circle = PI * (c ** 2)
trapezium = ((a + b) * c) / 2
square = b ** 2
rectangle = a * b

# 3. Output: Formatting to 3 decimal places
print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
