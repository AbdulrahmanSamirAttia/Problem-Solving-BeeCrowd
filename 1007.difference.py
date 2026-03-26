"""
Read four integer values named A, B, C and D.
Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).

Input
The input file contains 4 integer values.

Output
Print DIFERENCA (DIFFERENCE in Portuguese) with all the capital letters,
according to the following example, with a blank space before and after the equal signal.
"""

""" Solution (A) """
# Read four integer values named A, B, C and D.
A = int( input() )
B = int( input() )
C = int( input() )
D = int( input() )

# Calculate difference of THe inputs
difference = (A * B - C * D)


# Print difference of THe inputs
print(f"DIFERENCA = {difference}")

""" Solution (B) """
print(f"DIFERENCA = {(int( input() ) * int( input() ) - int( input() ) * int( input() ))}")
