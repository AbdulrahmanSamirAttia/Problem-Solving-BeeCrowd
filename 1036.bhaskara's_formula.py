"""
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula.
If it's impossible to calculate the roots because a division by zero or a square root of a negative number,
presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.

Input Samples	Output Samples
10.0 20.1 5.1   R1 = -0.29788
                R2 = -1.71212

0.0 20.0 5.0    Impossivel calcular


10.3 203.0 5.0  R1 = -0.02466
                R2 = -19.68408

10.0 3.0 5.0    Impossivel calcular
"""

""" Solution (A) """

import math

a,b,c = map(float, input().strip().split())

discriminant = b ** 2 - 4 * a * c

if discriminant < 0 or a  == 0:
    print("Impossivel calcular")
else:
    root_delta = math.sqrt(discriminant)

    R1 = ( -b + root_delta) / (2*a)
    R2 = ( -b - root_delta) / (2*a)

    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")



