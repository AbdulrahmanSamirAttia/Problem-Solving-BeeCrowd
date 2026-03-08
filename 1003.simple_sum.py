"""
Read two integer values, in this case, the variables A and B.
After this, calculate the sum between them and assign it to the variable SOMA.
Write the value of this variable.

Input
The input file contains 2 integer numbers.

Output
Print the message "SOMA" with all the capital letters,
with a blank space before and after the equal signal followed by the corresponding value to the sum of A and B.
Like all the problems, don't forget to print the end of line, otherwise you will receive "Presentation Error"
"""

""" Solution (A) """

# Input: Read Two Integer Variables Called A and B
A = int(input())
B = int(input())

# Process: Calculate Sum of A and B, Then assign it to the variable SOMA
SOMA = A + B

# Output: Print the message "SOMA" with all the capital letters,
print(f"SOMA = {SOMA}")

""" Solution (B) """

# Printing the message "SOMA" with Sum of Two Numbers,
print("SOMA =", int(input()) + int(input()))
