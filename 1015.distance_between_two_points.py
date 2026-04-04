"""
Read the four values corresponding to the x and y axes of two points in the plane,
p1 (x1, y1) and p2 (x2, y2) and calculate the distance between
them, showing four decimal places, according to the formula:

Distance =

Input
The input file contains two lines of data.
The first one contains two double values: x1 y1 and
the second one also contains two double values with one digit after the decimal point: x2 y2.

Output
Calculate and print the distance value using the provided formula, with 4 decimal places.
"""
import math

""" Solution (A) """
x1, y1 = map(float, input().strip().split())
x2, y2 = map(float, input().strip().split())

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{distance:.4f}")


""" Solution (B) """
p1 =  map( float, input().strip().split() )
p2 =  map( float, input().strip().split() )

distance = math.dist(p1, p2)

print(f"{distance:.4f}")

